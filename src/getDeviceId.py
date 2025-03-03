import subprocess

from PyQt5.QtWidgets import QLabel


def get_device_id(device_id_label: QLabel):
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    output = result.stdout.strip().split('\n')[1:]

    device_ids = [line.split('\t')[0] for line in output if line]

    if device_ids:
        device_id_label.setText(f"디바이스 아이디: {device_ids[0]}")
    else:
        device_id_label.setText("디바이스가 연결되지 않았습니다.")