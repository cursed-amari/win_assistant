from PyQt6 import QtWidgets, QtCore


class BufferFrame:
    def __init__(self, parent, context):
        self.frame = QtWidgets.QFrame(parent)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText(context)
        self.verticalLayout.addWidget(self.label)

    def __str__(self):
        return self.label.text()

    def get_frame(self):
        return self.frame
