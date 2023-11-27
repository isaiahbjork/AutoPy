import os
import subprocess
import importlib
import re
from generate_code import generate_code
from fix_code import fix_code
from improve_code import improve_code
from create_testing_code import create_testing_code
from check_syntax import check_syntax
from check_code import check_code
import json


def install_missing_packages(imports):
    for package in imports:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"Package '{package}' is not installed. Installing...")
            os.system(f"pip install {package}")


def write_code_to_file(code, file_path):
    with open(file_path, "w") as f:
        f.write(code)


def generate_and_test_code(prompt):
    while True:
        try:
            code = generate_code(prompt)
            imports = re.findall(r"(?:import|from) (\w+)", code)
            install_missing_packages(imports)
            print("I generated the code.")

            write_code_to_file(code, "output/output.py")
            syntax = check_syntax(code)
            print("Code Syntax", syntax)

            if syntax == True:
                testing_code = create_testing_code(code)
                test_syntax = check_syntax(testing_code)
                print("Testing Syntax", test_syntax)

                write_code_to_file(testing_code, "output/test_output.py")

                try:
                    test_script_path = os.path.join("output", "test_output.py")
                    result = subprocess.run(
                        ["python", test_script_path], capture_output=True, text=True
                    )
                    if result.returncode == 0:
                        print("Tests passed successfully.")
                        break
                    else:
                        print("Tests failed.")
                        print(result.stdout)
                        print(result.stderr)
                        testing_code = create_testing_code(
                            "Rewrite the testing code for this prompt there is a testing error: "
                            + "prompt: "
                            + prompt
                            + " Error: \n"
                            + f"{result.stdout}\n {result.stderr}"
                            + " Here is the code: "
                            + code
                            + " \n Here is the testing code: "
                            + testing_code
                        )
                        write_code_to_file(testing_code, "output/test_output.py")
                        continue

                except Exception as test_exec_exception:
                    print(
                        "I wrote testing code that has this error during execution:",
                        test_exec_exception,
                    )
                    testing_code = create_testing_code(
                        "Rewrite the testing code for this prompt there is a runtime error: "
                        + prompt
                        + "error: "
                        + str(test_exec_exception)
                        + " Here is the code: "
                        + code
                        + " /n Here is the testing code: "
                        + testing_code
                    )
                    write_code_to_file(testing_code, "output/test_output.py")
                    continue
            else:
                code = generate_code(
                    "Rewrite the code for this prompt there is a syntax error: "
                    + prompt
                    + "error: "
                    + syntax
                    + " Here is the code: "
                    + code
                )
                continue

        except Exception as main_exception:
            print("I wrote code that has this error:", main_exception)
            fixed_code = fix_code(
                str(main_exception),
                "Rewrite the code for this prompt there is an error: " + prompt + code,
            )

            write_code_to_file(fixed_code, "output/output.py")
            print("I am testing the fixed code.")
            try:
                testing_code = create_testing_code(
                    "Rewrite the code for this prompt there is a syntax error: "
                    + fixed_code
                )
                write_code_to_file(testing_code, "output/test_output.py")

                print("Fixed code execution and testing complete.")
                continue

            except Exception as fix_exception:
                print("The fixed code still has errors:", fix_exception)
                continue


# Define the prompt for which to generate code
prompt = input('What do you want AutoPy to build: ')

generate_and_test_code(prompt)
