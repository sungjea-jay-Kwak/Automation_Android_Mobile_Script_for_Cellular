import subprocess
from PyQt5.QtWidgets import QLabel


def get_device_id(device_id_label: QLabel):
    try:
        result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output = result.stdout.strip().split('\n')[1:]

        device_ids = [line.split('\t')[0] for line in output if line]

        if device_ids:
            device_id_label.setText(f"Device ID: {device_ids[0]}")
        else:
            device_id_label.setText("The devices are not connected")

    except subprocess.CalledProcessError as e:
        print("Error", e.output.decode())
