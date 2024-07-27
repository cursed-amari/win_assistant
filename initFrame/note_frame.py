from PyQt6 import QtWidgets, QtCore


class NoteFrame:
    def __init__(self, scrollArea, title, context, date, notification):
        self.scrollArea = scrollArea
        self.notification = notification
        self.date = date
        self.context = context
        self.title = title
        self.isAlarm = False
        self.app_func()

    def __str__(self):
        return self.title

    def app_func(self):
        self.init_frame()
        self.set_text()

    def init_frame(self):
        self.frame = QtWidgets.QFrame(self.scrollArea)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_title.setObjectName("label_title")
        self.verticalLayout_6.addWidget(self.label_title)
        self.textEdit_context = QtWidgets.QTextEdit(self.frame)
        self.textEdit_context.setAlignment(
        QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.textEdit_context.setReadOnly(True)
        self.textEdit_context.setObjectName("textEdit_context")
        self.verticalLayout_6.addWidget(self.textEdit_context)
        self.label_date = QtWidgets.QLabel(self.frame)
        self.label_date.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_date.setObjectName("label_date")
        self.verticalLayout_6.addWidget(self.label_date)
        self.verticalLayout_6.addWidget(self.label_date)
        self.frame_aditional = QtWidgets.QFrame(self.frame)
        self.frame_aditional.setMaximumSize(QtCore.QSize(16777207, 20))
        self.frame_aditional.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_aditional.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_aditional.setObjectName("frame_aditional")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_aditional)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_notification = QtWidgets.QLabel(self.frame_aditional)
        self.label_notification.setObjectName("label_notification")
        self.horizontalLayout_5.addWidget(self.label_notification)
        self.checkBox_complete = QtWidgets.QCheckBox(self.frame_aditional)
        self.checkBox_complete.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBox_complete.setText("")
        self.checkBox_complete.setObjectName("checkBox_complete")
        self.horizontalLayout_5.addWidget(self.checkBox_complete)
        self.verticalLayout_6.addWidget(self.frame_aditional)

    def set_text(self):
        self.label_title.setText(self.title)
        self.textEdit_context.setText(self.context)
        self.label_date.setText(self.date)
        self.label_notification.setText(self.notification if self.notification else "None")

    def get_frame(self):
        return self.frame
