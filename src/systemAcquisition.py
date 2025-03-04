import subprocess
import sys
import time

LOG_FILE = "boot_log.txt"

def get_boot_time():
    cmd = "adb shell cat /proc/uptime"
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode().strip()
        uptime_seconds = float(result.split()[0])
        current_time = time.time()
        return current_time - uptime_seconds
    except subprocess.CalledProcessError as e:
        print("ADB Execute Error:", e.output.decode())
        return None

def measure_boot_complete_time():
    try:
        print("Getting Booting time")
        boot_start_time = get_boot_time()
        print(f"Boot Start Time (Unix): {boot_start_time}")

        with open(LOG_FILE, "w", encoding="utf-8") as log_file:
            log_file.write(f"Boot Start Time (Unix): {boot_start_time}\n")
            log_file.write("=== Boot Log Start ===\n")

        cmd = "adb logcat -b all -v time"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                   encoding="utf-8", errors="replace")

        boot_completed_time = None

        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            for line in iter(process.stdout.readline, ''):
                log_file.write(line)

                if "BOOT_COMPLETED" in line:
                    boot_completed_time = time.time()
                    print(f"Boot Completed: {boot_completed_time}")
                    log_file.write(f"\nBoot Completed Time (Unix): {boot_completed_time}\n")
                    break

        process.terminate()

        if boot_start_time and boot_completed_time:
            total_boot_time = boot_completed_time - boot_start_time
            print(f"Total Boot Time: {total_boot_time:.2f} seconds")

            with open(LOG_FILE, "a", encoding="utf-8") as log_file:
                log_file.write(f"Total Boot Time: {total_boot_time:.2f} seconds\n")
                log_file.write("=== Boot Log End ===\n")

        print("Created boot_log.txt")

    except subprocess.CalledProcessError as e:
        print("ADB Execute Error:", e.output.decode())
        return None

