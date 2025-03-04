import subprocess

# Get device performance metrics
def get_performance_metrics():
    cpu_info, memory_info, network_info = "", "", ""

    cpu_adb = "adb shell dumpsys cpuinfo | grep TOTAL"
    memory_adb = "adb shell dumpsys meminfo | grep 'Used RAM'"

    try:
        cpu_info = subprocess.check_output(cpu_adb, shell=True, text=True).strip()
        memory_info = subprocess.check_output(memory_adb, shell=True, text=True).strip()

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    print(cpu_info, memory_info,network_info)