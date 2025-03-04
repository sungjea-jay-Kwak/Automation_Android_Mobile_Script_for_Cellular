import subprocess
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont

from src.NetworkInfo import get_network_data
from src.getDeviceId import get_device_id
from src.getSVCLog import save_boot_svc_log
from src.metricsInfo import get_performance_metrics
from src.systemAcquisition import measure_boot_complete_time

app = QApplication([])

window = QWidget()
window.setWindowTitle("Test Mobile Device")
window.setGeometry(100, 100, 400, 300)

layout = QVBoxLayout()

label = QLabel("Please Select Button What You Want to Test.", window)
label.setFont(QFont("Arial", 14))
layout.addWidget(label)

device_id_label = QLabel("DeviceID: None", window)
device_id_label.setFont(QFont("Arial", 12))
layout.addWidget(device_id_label)

btn = QPushButton("Get Device ID", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(lambda: get_device_id(device_id_label))
layout.addWidget(btn)

btn = QPushButton("Get Booting Time", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(measure_boot_complete_time)
layout.addWidget(btn)

# Not Implemented
btn = QPushButton("Get Location", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(get_network_data)
layout.addWidget(btn)

btn = QPushButton("Create SVC Logs", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(save_boot_svc_log)
layout.addWidget(btn)

btn = QPushButton("Get Network Status", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(get_network_data)
layout.addWidget(btn)

btn = QPushButton("Get System Performance", window)
btn.setFont(QFont("Arial", 14))
btn.clicked.connect(get_performance_metrics)
layout.addWidget(btn)

window.setLayout(layout)

window.show()

app.exec_()
