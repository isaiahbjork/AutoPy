def check_syntax(code):
    try:
        # The compile function will check the code's syntax.
        compile(code, "<string>", "exec")
        return True  # Syntax is correct
    except SyntaxError as e:
        return f"Syntax error: {e}"
