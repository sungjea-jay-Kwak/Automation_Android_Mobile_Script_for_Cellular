import subprocess

# Function to execute ADB commands
def adb_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"