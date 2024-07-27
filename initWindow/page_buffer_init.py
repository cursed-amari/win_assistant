from PyQt6 import QtWidgets, QtCore


class PageBufferInit:
    def __init__(self):
        self.page_buffer = QtWidgets.QWidget()
        self.page_buffer.setObjectName("page_buffer")
        self.verticalLayout_frame = QtWidgets.QVBoxLayout(self.page_buffer)
        self.verticalLayout_frame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_frame.setSpacing(0)
        self.verticalLayout_frame.setObjectName("verticalLayout_frame")
        self.scrollArea_buffer = QtWidgets.QScrollArea(self.page_buffer)
        self.scrollArea_buffer.setWidgetResizable(True)
        self.scrollArea_buffer.setObjectName("scrollArea_buffer")
        self.scrollAreaWidgetContents_buffer = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_buffer.setGeometry(QtCore.QRect(0, 0, 396, 553))
        self.scrollAreaWidgetContents_buffer.setObjectName("scrollAreaWidgetContents_buffer")
        self.verticalLayout_scrollArea = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_buffer)
        self.verticalLayout_scrollArea.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_scrollArea.setSpacing(0)
        self.verticalLayout_scrollArea.setObjectName("verticalLayout_scrollArea")
        self.scrollArea_buffer.setWidget(self.scrollAreaWidgetContents_buffer)
        self.verticalLayout_frame.addWidget(self.scrollArea_buffer)

    def get_widget(self):
        return self.page_buffer
