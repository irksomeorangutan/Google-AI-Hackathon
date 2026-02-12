import os

def execute_ping(target):
    # ❌ TRUE POSITIVE: Command Injection
    command = f"ping -c 1 {target}"
    return os.system(command)
