from PyQt6.QtCore import QDateTime
from loguru import logger

from initFrame.note_frame import NoteFrame
from utils import open_save


class PageNote:
    def __init__(self, main_window):
        self.main_window = main_window

    @logger.catch
    def open_create_note(self, bul_val=False):
        if self.main_window.main_windowwindow_status == 0:
            self.main_window.main_windowfull_window(True)
        self.main_window.main_windowpage_create_note.dateTimeEdit_create_note.setDateTime(QDateTime.currentDateTime())
        self.main_window.main_windowpage_create_note.dateTimeEdit_create_note.setMinimumDateTime(QDateTime.currentDateTime())
        self.main_window.main_windowstackedWidget.setCurrentIndex(1)

    @logger.catch
    def create_note(self, bul_val=False):
        if self.main_window.main_windowpage_create_note.lineEdit_create_note_name.text() in self.main_window.main_windowsave_data.keys():
            print("No")
        else:
            note_frame = self.main_window.main_windowcreate_note_frame(self.main_window.main_windowpage_create_note.lineEdit_create_note_name.text(),
                                                self.main_window.main_windowpage_create_note.textEdit_create_note_text.toPlainText(),
                                                QDateTime.currentDateTime().toString(),
                                                self.main_window.main_windowpage_create_note.dateTimeEdit_create_note.dateTime().toString() if
                                                self.main_window.main_windowpage_create_note.checkBox_create_note_notification_activate.isChecked() else False)
            self.main_window.main_windowadd_to_save_data()
            self.main_window.main_windowpage_create_note.lineEdit_create_note_name.setText("")
            self.main_window.main_windowpage_create_note.textEdit_create_note_text.setText("")
            self.main_window.main_windowpage_note.verticalLayout_scrollArea.insertWidget(0, note_frame)
            self.main_window.main_windowstackedWidget.setCurrentIndex(0)

    @logger.catch
    def create_note_frame(self, title, context, date, notification):
        note = NoteFrame(self.main_window.main_windowpage_note.scrollAreaWidgetContents_page_note,
                         title,
                         context,
                         date,
                         notification)
        self.main_window.main_windowcurrent_notes.append(note)
        note.checkBox_complete.clicked.connect(self.main_window.main_windowdelete_note)
        note.label_title.mouseDoubleClickEvent = lambda event: self.main_window.main_windowupdate_note(event, note)
        self.main_window.main_windowcreate_alarm(note)

        return note.get_frame()

    @logger.catch
    def update_note(self, event, note):
        self.main_window.main_windowstackedWidget.setCurrentIndex(1)
        self.main_window.main_windowpage_create_note.lineEdit_create_note_name.setText(note.title)
        self.main_window.main_windowpage_create_note.textEdit_create_note_text.setText(note.context)
        print(note.date)

    @logger.catch
    def delete_note(self, bul_val):
        for i in self.main_window.main_windowcurrent_notes:
            if self.main_window.main_windowsender().parent().parent() == i.get_frame():
                if i.isAlarm:
                    self.main_window.main_windowframe_navigate_color_change(False)
                i.get_frame().deleteLater()
                self.main_window.main_windowsave_data.pop(i.title)
                self.main_window.main_windowsave_note()
    
    @logger.catch
    def load_saves(self):
        self.main_window.save_data = open_save()
        if self.main_window.save_data:
            for k, v in self.main_window.save_data.items():
                note = self.create_note_frame(k,
                                              v["context"],
                                              v["date"],
                                              v["notification"])
                self.main_window.page_note.verticalLayout_scrollArea.insertWidget(0, note)
