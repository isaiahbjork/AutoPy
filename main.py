import os
import openai
import pylint.lint
from pylint import epylint as lint
from io import StringIO
import sys

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
            "content": f"Write python code to solve this error: {error} for this python code:\n{broken_code}\n"
        }],
        temperature=0.7,
        max_tokens=1000,
        stop=None,
        n=1,
        presence_penalty=0,
        frequency_penalty=0)
    code = response.choices[0].message.content
    code = code.replace("`", "")
    return code


def generate_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": system
        }, {
            "role": "user",
            "content": f"Write python code for:\n{prompt}\n"
        }],
        temperature=0.7,
        max_tokens=1000,
        stop=None,
        n=1,
        presence_penalty=0,
        frequency_penalty=0)
    code = response.choices[0].message.content
    code = code.replace("`", "")
    return code


# Define the prompt for which to generate code
prompt = "print through a list from 1 to 20 one at a time and at the end print finished."

while True:
    # Generate code based on the prompt
    code = generate_code(prompt)
    print("Generated code:", code)

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