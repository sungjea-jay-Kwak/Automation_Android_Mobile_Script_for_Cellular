import subprocess
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont  # QFont를 import

from src.getDeviceId import get_device_id
from src.getSVCLog import save_boot_svc_log

app = QApplication([])

window = QWidget()
window.setWindowTitle("디바이스 아이디 가져오기")
window.setGeometry(100, 100, 400, 300)

layout = QVBoxLayout()

label = QLabel("여기에 텍스트가 표시됩니다.", window)
label.setFont(QFont("Arial", 14))
layout.addWidget(label)

device_id_label = QLabel("디바이스 아이디: 없음", window)
device_id_label.setFont(QFont("Arial", 12))
layout.addWidget(device_id_label)

btn = QPushButton("Device ID List", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(lambda: get_device_id(device_id_label))
layout.addWidget(btn)

btn = QPushButton("Crete SVC Logs", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(save_boot_svc_log)
layout.addWidget(btn)

window.setLayout(layout)

window.show()

app.exec_()
