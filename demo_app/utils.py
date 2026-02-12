import subprocess

# ❌ TRUE POSITIVE
def run_user_command(cmd):
    return subprocess.call(cmd, shell=True)


# ✅ FALSE POSITIVE (Sanitized Input)
def safe_run_user_command(cmd):
    allowed_commands = ["date", "whoami"]

    if cmd not in allowed_commands:
        return "Command not allowed"

    # Safe usage: no shell=True and strict allowlist
    return subprocess.call([cmd])
