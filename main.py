import os
import openai
import pylint.lint
from pylint import epylint as lint
from io import StringIO
import sys
import importlib
import re
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')

system = "You are PythonGPT and expert python coder. Only response in python syntax. Use # comments for any text words so you dont break the code. You can develop python scripts until they are perfect. You use completely autonomous."


def fix_code(error, broken_code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": system
        }, {
            "role": "user",
            "content": f"Write python code to solve this error: {error} for this python code:\n{broken_code}\n, respond in python syntax, if you write a sentence use a #"
        }],
        temperature=0.7,
        max_tokens=1000,
        stop=None,
        n=1,
        presence_penalty=0,
        frequency_penalty=0)
    code = response.choices[0].message.content
    # Get the index of the desired word in the list
    index = code.index("`python")

    # Slice the list to remove everything before the desired word
    new_words = code[index:]

    # Join the list back into a string
    code = " ".join(new_words)
   
    return code


def generate_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": system
        }, {
            "role": "user",
            "content": f"Write python code for, respond in python syntax, if you write a sentence use a #:\n{prompt}\n"
        }],
        temperature=0.7,
        max_tokens=1000,
        stop=None,
        n=1,
        presence_penalty=0,
        frequency_penalty=0)
    code = response.choices[0].message.content
    # Get the index of the first occurrence of "```python"
    start_index = code.index("```python") + len("```python") + 1

    # Get the index of the last occurrence of "```"
    end_index = code.rindex("```")

    # Extract the Python code between the start and end indices
    code = code[start_index:end_index]
    return code


# Define the prompt for which to generate code
prompt = "Generate a plot of sin(x) and cos(x) from 0 to 2*pi using matplotlib, with a legend and axis labels."

while True:
    # Generate code based on the prompt
    code = generate_code(prompt)
    print("Code Generated")

    # Write the generated code to a Python file
    with open("generated_code.py", "w") as f:
        f.write(code)

    # Check if the generated code is error-free
    stdout, stderr = StringIO(), StringIO()
    try:
        exec(code)
        print("Generated code is error-free!")
        break
    except Exception as e:
        print("Generated code has an error:", e)
        # Use the 'fix_code' function to generate a fixed code snippet
        fixed_code = fix_code(str(e), code)
        print("Fixed code:", fixed_code)
        # Parse the fixed code for import statements
        imports = re.findall(r"import (\w+)", fix_code)
        for package in imports:
            try:
                importlib.import_module(package)
            except ImportError:
                print(f"Package '{package}' is not installed. Installing...")
                os.system(f"pip install {package}")

        # Write the fixed code to a Python file
        with open("fixed_code.py", "w") as f:
            f.write(fixed_code)

        # Evaluate the fixed code snippet to see if it works
        print("Executing fixed code...")
        try:
            exec(fixed_code)
            print("Fixed code is error-free!")
            break
        except Exception as e:
            print("Fixed code has an error:", e)
            continue


print("Done!")
