import os

def debug_admin_tool():
    user_input = "hardcoded_safe_value"

    # ❌ Vulnerable pattern
    os.system("ls " + user_input)
