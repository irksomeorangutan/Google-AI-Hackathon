from services import execute_ping

def handle_ping(user_input):
    # No validation - tainted input flows directly
    result = execute_ping(user_input)
    return f"Command output: {result}"
