import subprocess
import time


def is_device_connected():
    cmd = "adb devices"
    result = subprocess.check_output(cmd, shell=True).decode().strip().split("\n")
    devices = [line for line in result if "\tdevice" in line]
    return len(devices) > 0

def save_boot_svc_log():
    while not is_device_connected():
        time.sleep(0.1)

    print("Collecting SVC logs...")
    try:
        cmd = "adb logcat -b all -v time"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")

        with open("boot_svc_log.txt", "w") as log_file:
            for line in iter(process.stdout.readline, ''):
                if "!@Boot_SVC: PhoneApp OnCreate" in line:
                    print(line.strip())
                    log_file.write(line)
                if "!@Boot_SVC: setRadioPower on" in line:
                    print(line.strip())
                    log_file.write(line)
                if "!@Boot_SVC: CS Registered" in line:
                    print(line.strip())
                    log_file.write(line)
                if "!@Boot_SVC: GPRS Attached" in line:
                    print(line.strip())
                    log_file.write(line)
                if "!@Boot_SVC : SIM onAllRecordsLoaded" in line:
                    print(line.strip())
                    log_file.write(line)
                if "!@Boot_SVC : setupDataCall" in line:
                    print(line.strip())
                    log_file.write(line)
                    break

        process.terminate()
        print("Created boot_svc_log.txt")

    except subprocess.CalledProcessError as e:
        print("Error", e.output.decode())