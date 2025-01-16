import time
from datetime import datetime

from PyQt6.QtCore import QThread, pyqtSignal


class AlarmThread(QThread):
    alarm_signal = pyqtSignal()

    def __init__(self, alarm_time, frame):
        super().__init__()
        self.frame = frame
        dt = datetime.strptime(alarm_time, "%a %b %d %H:%M:%S %Y")
        self.alarm_time = dt.timestamp()

    def run(self):
        while True:
            current_time = self.get_current_time()
            if current_time >= self.alarm_time:
                self.frame.get_frame().setStyleSheet('background-color: rgb(255, 0, 0);')
                self.frame.isAlarm = True
                self.alarm_signal.emit()
                break
            self.sleep(1)

    def get_current_time(self):
        return int(time.time())
