from PyQt6 import QtWidgets, QtCore


class BufferFrame:
    def __init__(self, parent, context):
        self.frame = QtWidgets.QFrame(parent)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame.setMaximumSize(QtCore.QSize(400, 16777207))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText(context)
        self.verticalLayout.addWidget(self.label)
        self.frame_aditional = QtWidgets.QFrame(self.frame)
        self.frame_aditional.setMaximumSize(QtCore.QSize(16777207, 20))
        self.frame_aditional.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_aditional.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_aditional.setObjectName("frame_aditional")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_aditional)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_notification = QtWidgets.QLabel(self.frame_aditional)
        self.label_notification.setObjectName("label_notification")
        self.horizontalLayout.addWidget(self.label_notification)
        self.checkBox_pin = QtWidgets.QCheckBox(self.frame_aditional)
        self.checkBox_pin.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkBox_pin.setText("")
        self.checkBox_pin.setObjectName("checkBox_complete")
        self.horizontalLayout.addWidget(self.checkBox_pin)
        self.verticalLayout.addWidget(self.frame_aditional)

    def __str__(self):
        return self.label.text()

    def get_frame(self):
        return self.frame
