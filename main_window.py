import time

import keyboard
from PyQt6 import QtWidgets
from PyQt6.QtCore import QDateTime, QSize, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMessageBox

from loguru import logger
import json

from alarm_tread import AlarmThread
from initFrame.buffer_frame import BufferFrame
from initWindow.main_window_init import Ui_MainWindow
from initFrame.note_frame import NoteFrame
from utils import open_save, get_taskbar_height


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    copySignal = pyqtSignal()

    @logger.catch
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.list_navigate = [self.pushButton_minmax, self.pushButton_create_note,
                              self.pushButton_buffer, self.pushButton_mail]
        self.clipboard = QApplication.clipboard()
        self.window_status = 0
        self.save_data = {}
        self.current_notes = []
        self.current_buffer = []

        self.app_func()

    @logger.catch
    def app_func(self):
        self.centralwidget.enterEvent = self.onEnter
        self.centralwidget.leaveEvent = self.onLeave

        self.pushButton_minmax.clicked.connect(self.full_window)
        self.pushButton_mail.clicked.connect(lambda: self.close())
        self.pushButton_create_note.clicked.connect(self.open_create_note)
        self.page_create_note.pushButton_create_note_save.clicked.connect(self.create_note)
        self.pushButton_buffer.clicked.connect(self.open_buffer)
        self.copySignal.connect(self.onCtrlCPressed)

        self.frame_list.setVisible(False)
        self.setFixedSize(10, 200)

        self.frame_navigate.setMinimumSize(QSize(40, 120))
        counter = 0
        for i in self.list_navigate:
            i.setMinimumSize(QSize(40, 23))
            self.gridLayout.removeWidget(i)
            self.gridLayout.addWidget(i, counter, 0)
            counter += 1

        self.window_move(10, 200)

        self.stackedWidget.setCurrentIndex(0)

        self.load_saves()
        self.setupClipboardListener()

    @logger.catch
    def full_window(self, bul_val):
        if self.window_status == 0:
            self.window_status = 1
            self.stackedWidget.setCurrentIndex(0)
            self.position_widgets(0)
            self.setFixedSize(400, 600)
            self.centralwidget.setFixedSize(400, 600)
            self.window_move(400, 600)
            self.frame_list.setVisible(True)
            self.pushButton_minmax.setText('>')
        else:
            self.window_status = 0
            self.position_widgets(1)
            self.setFixedSize(10, 200)
            self.centralwidget.setFixedSize(10, 200)
            self.window_move(10, 200)
            self.frame_list.setVisible(False)
            self.pushButton_minmax.setText('<')

    @logger.catch
    def position_widgets(self, num: int):
        """
        1 = vertical
        0 = horizontal
        """
        counter_vertical = 0
        counter_horizontal = 0
        for i in self.list_navigate:
            self.gridLayout.removeWidget(i)
            self.gridLayout.addWidget(i, counter_vertical, counter_horizontal)
            if num == 1:
                counter_vertical += 1
            else:
                counter_horizontal += 1

    @logger.catch
    def onEnter(self, event):
        if self.window_status == 0:
            self.setFixedSize(60, 200)
            self.centralwidget.setFixedSize(60, 200)
            self.window_move(60, 200)

    @logger.catch
    def onLeave(self, event):
        if self.window_status == 0:
            self.setFixedSize(10, 200)
            self.setFixedSize(10, 200)
            self.window_move(10, 200)

    @logger.catch
    def window_move(self, x: int, y: int):
        screen_size_x, screen_size_y = get_taskbar_height()
        screen_size_x -= x
        screen_size_y -= y
        self.move(screen_size_x, screen_size_y)

    @logger.catch
    def open_create_note(self, bul_val=False):
        if self.window_status == 0:
            self.full_window(True)
        self.page_create_note.dateTimeEdit_create_note.setDateTime(QDateTime.currentDateTime())
        self.page_create_note.dateTimeEdit_create_note.setMinimumDateTime(QDateTime.currentDateTime())
        self.stackedWidget.setCurrentIndex(1)

    @logger.catch
    def create_note(self, bul_val=False):
        if self.page_create_note.lineEdit_create_note_name.text() in self.save_data.keys():
            error = QMessageBox(text='Имя уже занято')
            error.exec()
        else:
            note_frame = self.create_note_frame(self.page_create_note.lineEdit_create_note_name.text(),
                                          self.page_create_note.textEdit_create_note_text.toPlainText(),
                                          QDateTime.currentDateTime().toString(),
                                          self.page_create_note.dateTimeEdit_create_note.dateTime().toString() if
                                          self.page_create_note.checkBox_create_note_notification_activate.isChecked() else False)
            self.add_to_save_data()
            self.page_create_note.lineEdit_create_note_name.setText("")
            self.page_create_note.textEdit_create_note_text.setText("")
            self.page_note.verticalLayout_scrollArea.insertWidget(0, note_frame)
            self.stackedWidget.setCurrentIndex(0)

    @logger.catch
    def create_note_frame(self, title, context, date, notification):
        note = NoteFrame(self.page_note.scrollAreaWidgetContents_page_note,
                         title,
                         context,
                         date,
                         notification)
        self.current_notes.append(note)
        note.checkBox_complete.clicked.connect(self.delete_note)
        note.label_title.mouseDoubleClickEvent = lambda event: self.update_note(event, note)
        self.create_alarm(note)

        return note.get_frame()

    @logger.catch
    def update_note(self, event, note):
        self.stackedWidget.setCurrentIndex(1)
        self.page_create_note.lineEdit_create_note_name.setText(note.title)
        self.page_create_note.textEdit_create_note_text.setText(note.context)
        print(note.date)

    @logger.catch
    def delete_note(self, bul_val):
        for i in self.current_notes:
            if self.sender().parent().parent() == i.get_frame():
                if i.isAlarm:
                    self.frame_navigate_color_change(False)
                i.get_frame().deleteLater()
                self.save_data.pop(i.title)
                self.save_note()

    @logger.catch
    def load_saves(self):
        self.save_data = open_save()
        if self.save_data:
            for k, v in self.save_data.items():
                note = self.create_note_frame(k,
                                              v["context"],
                                              v["date"],
                                              v["notification"])
                self.page_note.verticalLayout_scrollArea.insertWidget(0, note)

    @logger.catch
    def create_alarm(self, frame):
        if frame.label_notification.text() != 'None':
            self.alarm_tread = []
            alarm = AlarmThread(frame.label_notification.text(), frame)
            alarm.start()
            alarm.alarm_signal.connect(lambda: self.frame_navigate_color_change(True))
            self.alarm_tread.append(alarm)

    @logger.catch
    def frame_navigate_color_change(self, bool):
        """Does not work"""
        if bool:
            self.frame_navigate.setStyleSheet('background-color: red;')
        else:
            self.frame_navigate.setStyleSheet('background-color: 255, 255, 255;')

    @logger.catch
    def add_to_save_data(self):
        self.save_data[self.page_create_note.lineEdit_create_note_name.text()] = {"context": self.page_create_note.textEdit_create_note_text.toPlainText(),
                                                                 "date": QDateTime.currentDateTime().toString(),
                                                                 "notification": self.page_create_note.dateTimeEdit_create_note.dateTime().toString() if
                                                                 self.page_create_note.checkBox_create_note_notification_activate.isChecked() else False
                                                                 }
        self.save_note()

    @logger.catch
    def save_note(self):
        with open("./note_save.json", "w") as file:
            json.dump(self.save_data, file, indent=4)

    @logger.catch
    def open_buffer(self, event):
        if self.window_status == 0:
            self.full_window(True)
        self.stackedWidget.setCurrentIndex(2)

    @logger.catch
    def setupClipboardListener(self):
        keyboard.add_hotkey('ctrl+c', lambda: self.copySignal.emit())

    @logger.catch
    def onCtrlCPressed(self):
        time.sleep(0.005)
        mime_data = self.clipboard.mimeData()

        if mime_data.hasText():
            clipboard_content = mime_data.text()
            self.create_buffer_frame(clipboard_content)
        elif mime_data.hasUrls():
            urls = mime_data.urls()
            self.create_buffer_frame(urls[0].toString())
        else:
            pass

    @logger.catch
    def create_buffer_frame(self, context):
        if len(self.current_buffer) >= 5:
            self.current_buffer[0].get_frame().deleteLater()
            self.current_buffer.pop(0)
        buffer = BufferFrame(self.page_buffer.scrollAreaWidgetContents_buffer, context)
        buffer.label.mouseDoubleClickEvent = lambda event: self.get_buffer(event, buffer.label.text())
        self.current_buffer.append(buffer)
        self.page_buffer.verticalLayout_scrollArea.insertWidget(0, buffer.get_frame())

    @logger.catch
    def get_buffer(self, event, context):
        self.clipboard.setText(context)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
