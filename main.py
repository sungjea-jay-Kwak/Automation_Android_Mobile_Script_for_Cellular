import subprocess
import pandas as pd
import pytest
import time
import subprocess
import re


# Function to execute ADB commands
def adb_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


# Get LTE/5G signal parameters
def get_network_data():
    network_data = {
        "RSRP": None,
        "RSRQ": None,
        "SINR": None,
        "Network Type": None
    }

    try:
        output = subprocess.check_output(["adb", "shell", "dumpsys", "telephony.registry"], universal_newlines=True)

        for line in output.split("\n"):
            if "rsrp=" in line.lower():
                network_data["RSRP"] = re.search(r"rsrp=(-?\d+)", line)
                network_data["RSRP"] = network_data["RSRP"].group(1) if network_data["RSRP"] else None
            if "rsrq=" in line.lower():
                network_data["RSRQ"] = re.search(r"rsrq=(-?\d+)", line)
                network_data["RSRQ"] = network_data["RSRQ"].group(1) if network_data["RSRQ"] else None
            if "rssnr=" in line.lower():
                network_data["SINR"] = re.search(r"rssnr=(-?\d+)", line)
                network_data["SINR"] = network_data["SINR"].group(1) if network_data["SINR"] else None
            if "mDataNetworkType" in line:
                network_data["Network Type"] = line.split("=")[-1].strip()

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    return network_data


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


# PyTest case
@pytest.mark.parametrize("iteration", range(3))  # Run test multiple times
def test_network_performance(iteration):
    network_data = get_network_data()
    perf_data = get_performance_metrics()

    # Merge results
    data = {**network_data, **perf_data, "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

    # Save to CSV
    df = pd.DataFrame([data])
    df.to_csv("network_performance_logs.csv", mode='a', index=False, header=False)

    print("✅ Test Iteration:", iteration + 1, "Data:", data)


if __name__ == "__main__":
    pytest.main(["-s", "main.py"])