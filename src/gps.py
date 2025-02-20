import subprocess
import re

def gps_info():
    try:
        command = "adb shell dumpsys location"
        output = subprocess.check_output(command, shell=True, text=True)

        match = re.search(r'Location\[(gps|network|fused) ([\d\.\-]+),([\d\.\-]+)', output)

        if match:
            lat = match.group(2)  # Latitude
            lon = match.group(3)  # Longitude
            print(f"Latitude: {lat}, Longitude: {lon}")
        else:
            print("Can't find Lon and Lat")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
