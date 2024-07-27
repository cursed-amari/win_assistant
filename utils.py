import json
import os
from win32api import GetMonitorInfo, MonitorFromPoint


def open_save():
    if os.path.exists("./note_save.json"):
        try:
            with open("./note_save.json", "r") as file:
                save = json.load(file)
            return save
        except ValueError as e:
            print("JSON object issue:", e)

def get_taskbar_height():
    monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
    work_area = monitor_info.get("Work")
    return work_area[2], work_area[3]