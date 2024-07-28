# Form implementation generated from reading ui file 'winSup.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QSize, Qt

from initWindow.page_buffer_init import PageBufferInit
from initWindow.page_create_note_init import PageCreateNoteInit
from initWindow.page_note_init import PageNoteInit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)

        MainWindow.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.FramelessWindowHint)

        MainWindow.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_navigate = QtWidgets.QFrame(self.centralwidget)
        self.frame_navigate.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_navigate.setStyleSheet("")
        self.frame_navigate.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_navigate.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_navigate.setObjectName("frame_navigate")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_navigate)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_minmax = QtWidgets.QPushButton(self.frame_navigate)
        self.pushButton_minmax.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_minmax.setObjectName("pushButton_minmax")
        self.gridLayout.addWidget(self.pushButton_minmax, 0, 0, 1, 1)
        self.pushButton_create_note = QtWidgets.QPushButton(self.frame_navigate)
        self.pushButton_create_note.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_create_note.setObjectName("pushButton_create_note")
        self.gridLayout.addWidget(self.pushButton_create_note, 0, 1, 1, 1)
        self.pushButton_buffer = QtWidgets.QPushButton(self.frame_navigate)
        self.pushButton_buffer.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_buffer.setObjectName("pushButton_buffer")
        self.gridLayout.addWidget(self.pushButton_buffer, 0, 2, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_navigate)
        self.pushButton_exit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout.addWidget(self.pushButton_exit, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame_navigate)
        self.frame_list = QtWidgets.QFrame(self.centralwidget)
        self.frame_list.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list.setObjectName("frame_list")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_list)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_list)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_note = PageNoteInit()
        self.stackedWidget.addWidget(self.page_note.get_widget())
        self.page_create_note = PageCreateNoteInit()
        self.stackedWidget.addWidget(self.page_create_note.get_widget())
        self.page_buffer = PageBufferInit()
        self.stackedWidget.addWidget(self.page_buffer.get_widget())
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_list)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_minmax.setText(_translate("MainWindow", "<"))
        self.pushButton_create_note.setText(_translate("MainWindow", "+"))
        self.pushButton_buffer.setText(_translate("MainWindow", "буфер"))
        self.pushButton_exit.setText(_translate("MainWindow", "exit"))
        self.page_create_note.checkBox_create_note_notification_activate.setText(_translate("MainWindow", "CheckBox"))
        self.page_create_note.pushButton_create_note_save.setText(_translate("MainWindow", "save"))
        self.page_create_note.pushButton_create_note_cancel.setText(_translate("MainWindow", "cancel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
