import subprocess
import time


def is_device_connected():
    cmd = "adb devices"
    result = subprocess.check_output(cmd, shell=True).decode().strip().split("\n")
    devices = [line for line in result if "\tdevice" in line]
    return len(devices) > 0


def get_boot_time():
    cmd = "adb shell cat /proc/uptime"
    result = subprocess.check_output(cmd, shell=True).decode().strip()
    uptime_seconds = float(result.split()[0])
    current_time = time.time()
    return current_time - uptime_seconds


def measure_boot_complete_time():
    boot_start_time = get_boot_time()
    print(f"🔹 Boot Start Time (Unix): {boot_start_time}")

    cmd = "adb logcat -b all -v time"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                               encoding="utf-8", errors="replace")

    boot_completed_time = None

    for line in iter(process.stdout.readline, ''):
        print(line.strip())

        if "BOOT_COMPLETED" in line:
            boot_completed_time = time.time()
            print(f"Boot Completed: {boot_completed_time}")
            break

    process.terminate()

    if boot_start_time and boot_completed_time:
        total_boot_time = boot_completed_time - boot_start_time
        print(f"Total Boot Time: {total_boot_time:.2f} seconds")


if __name__ == "__main__":
    print("🚀 Waiting for device to connect...")


    while not is_device_connected():
        time.sleep(0.1)

    print("Device connected! Measuring boot time...")
    measure_boot_complete_time()