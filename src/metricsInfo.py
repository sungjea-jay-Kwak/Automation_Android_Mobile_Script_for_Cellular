from src.adbCommand import adb_command

# Get device performance metrics
def get_performance_metrics():
    cpu_info = adb_command("adb shell dumpsys cpuinfo | grep TOTAL")
    memory_info = adb_command("adb shell dumpsys meminfo | grep 'Used RAM'")
    network_info = adb_command("adb shell dumpsys netstats | grep 'iface=wlan0'")

    return {
        "CPU Usage": cpu_info,
        "Memory Usage": memory_info,
        "Network Stats": network_info
    }