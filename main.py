import os
import openai
from pylint import epylint as lint
from io import StringIO
import importlib
import re
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')

system = "You are PythonGPT and expert python coder. Only respond in python syntax. Use # comments for any text words so you dont break the code. You can develop python scripts until they are perfect. You use completely autonomy."


def fix_code(error, broken_code):
    print('I am fixing code.')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": system
        }, {
            "role": "user",
            "content": f"Write python code to solve this error: {error} for this python code:\n{broken_code}\n, respond in python syntax, if you write a sentence use a # at the start of it so code doesn't break."
        }],
        temperature=0.7,
        max_tokens=1000,
        stop=None,
        n=1,
        presence_penalty=0,
        frequency_penalty=0)
    code = response.choices[0].message.content
    try:
        start_index = code.index("```python") + len("```python") + 1

        # Get the index of the last occurrence of "```"
        end_index = code.rindex("```")

        # Extract the Python code between the start and end indices
        code = code[start_index:end_index]
        return code
    except ValueError:
        print("I had an problem parsing the code so it might contain errors.")
        return code


def generate_code(prompt):
    print('I am writing the code.')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": system
        }, {
            "role": "user",
            "content": f"Respond in python syntax, if you write a sentence use a # at the start of it so code doesn't break., Write python complete code, including all necessary functions for:\n{prompt}\n"
        }],
        temperature=0.7,
        max_tokens=2500,
        stop=None,
        n=1,
        presence_penalty=0,
        frequency_penalty=0)
    code = response.choices[0].message.content
    # Get the index of the first occurrence of "```python"
    try:
        start_index = code.index("```python") + len("```python") + 1

        # Get the index of the last occurrence of "```"
        end_index = code.rindex("```")

        # Extract the Python code between the start and end indices
        code = code[start_index:end_index]
        return code
    except ValueError:
        print("I had an problem parsing the code so it might contain errors.")
        return code


# Define the prompt for which to generate code
while True:
    try:
        # Generate code based on the prompt
        prompt = input('What do you want AutoPy to build: ')
        code = generate_code(prompt)
        imports = re.findall(r"(?:import|from) (\w+)", code)
        for package in imports:
            try:
                importlib.import_module(package)
            except ImportError:
                print(
                    f"Package '{package}' is not installed. Installing...")
                os.system(f"pip install {package}")
        print("I generated the code.")
    except Exception as e:
        print('I had an error writing the code. I will rewrite it.')
        continue

    # Write the generated code to a Python file
    with open('code.py', "w") as f:
        f.write(code)

    # Check if the generated code is error-free
    stdout, stderr = StringIO(), StringIO()
    try:
        print('I am testing the code.')
        exec(code)
        print("I wrote error free code.")
        break
    except Exception as main_exception:

        print("I wrote code that has this error:", main_exception)
        # Use the 'fix_code' function to generate a fixed code snippet
        fixed_code = fix_code(str(main_exception), code)
        print("I fixed the code for errors.")
        imports = re.findall(r"(?:import|from) (\w+)", fixed_code)
        for package in imports:
            try:
                importlib.import_module(package)
            except ImportError:
                print(
                    f"Package '{package}' is not installed. Installing...")
                os.system(f"pip install {package}")

        # Evaluate the fixed code snippet to see if it works
        print("I am testing the fixed code.")
        try:
            exec(fixed_code)
            print("I wrote error-free code!")
            break
        except Exception as fix_exception:
            print("I wrote code that has an error:", fix_exception)
            continue
