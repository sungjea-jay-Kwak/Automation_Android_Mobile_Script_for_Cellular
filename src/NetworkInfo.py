import subprocess
import re


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

    print(network_data)