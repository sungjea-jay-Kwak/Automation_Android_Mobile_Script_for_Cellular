import subprocess
import pandas as pd
import pytest
import time


# Function to execute ADB commands
def adb_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


# Get LTE/5G signal parameters
def get_network_info():
    output = adb_command("adb shell dumpsys telephony.registry")
    network_data = {
        "RSRP": None,
        "RSRQ": None,
        "SINR": None,
        "Network Type": None
    }

    for line in output.split("\n"):
        if "mLteRsrp" in line:
            network_data["RSRP"] = line.split("=")[-1].strip()
        elif "mLteRsrq" in line:
            network_data["RSRQ"] = line.split("=")[-1].strip()
        elif "mLteRssnr" in line:
            network_data["SINR"] = line.split("=")[-1].strip()
        elif "mDataNetworkType" in line:
            network_data["Network Type"] = line.split("=")[-1].strip()

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
    network_data = get_network_info()
    perf_data = get_performance_metrics()

    # Merge results
    data = {**network_data, **perf_data, "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

    # Save to CSV
    df = pd.DataFrame([data])
    df.to_csv("network_performance_logs.csv", mode='a', index=False, header=False)

    print("✅ Test Iteration:", iteration + 1, "Data:", data)


if __name__ == "__main__":
    pytest.main(["-s", "main.py"])