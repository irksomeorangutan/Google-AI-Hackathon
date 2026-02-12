from utils import run_user_command, safe_run_user_command

def handle_exec(user_input):
    return str(run_user_command(user_input))

def handle_safe_exec(user_input):
    return str(safe_run_user_command(user_input))
