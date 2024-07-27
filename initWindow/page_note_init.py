from PyQt6 import QtWidgets, QtCore


class PageNoteInit:
    def __init__(self):
        self.page_note = QtWidgets.QWidget()
        self.page_note.setObjectName("page_note")
        self.verticalLayout_frame = QtWidgets.QVBoxLayout(self.page_note)
        self.verticalLayout_frame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_frame.setSpacing(0)
        self.verticalLayout_frame.setObjectName("verticalLayout_frame")
        self.scrollArea_page_note = QtWidgets.QScrollArea(self.page_note)
        self.scrollArea_page_note.setWidgetResizable(True)
        self.scrollArea_page_note.setObjectName("scrollArea_page_note")
        self.scrollAreaWidgetContents_page_note = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_page_note.setGeometry(QtCore.QRect(0, 0, 396, 553))
        self.scrollAreaWidgetContents_page_note.setObjectName("scrollAreaWidgetContents_page_note")
        self.verticalLayout_scrollArea = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_page_note)
        self.verticalLayout_scrollArea.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_scrollArea.setSpacing(0)
        self.verticalLayout_scrollArea.setObjectName("verticalLayout_scrollArea")
        self.scrollArea_page_note.setWidget(self.scrollAreaWidgetContents_page_note)
        self.verticalLayout_frame.addWidget(self.scrollArea_page_note)

    def get_widget(self):
        return self.page_note
