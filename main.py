import sys
import time
import subprocess
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton


class TestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("테스트 준비 중...")
        self.button = QPushButton("부팅 테스트 실행")
        self.button.clicked.connect(self.run_boot_test)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def run_boot_test(self):
        self.label.setText("⏳ 부팅 테스트 실행 중...")
        print("✅ 디바이스 연결됨! 부팅 테스트 실행")  # 여전히 콘솔에 출력되지만...

        # 부팅 테스트 실행
        script_path = "src/systemAcquisition.py"

        # subprocess.run으로 실행하여 결과를 기다림
        try:
            result = subprocess.run([sys.executable, script_path], check=True, text=True, capture_output=True)
            # 출력된 로그를 GUI에 표시
            self.label.setText(f"테스트 완료: {result.stdout}")
            print(f"부팅 테스트 완료: {result.stdout}")

        except subprocess.CalledProcessError as e:
            self.label.setText(f"테스트 실패: {e}")
            print(f"테스트 중 오류 발생: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestApp()
    window.show()
    sys.exit(app.exec_())
