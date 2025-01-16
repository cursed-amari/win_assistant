import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QHBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()  # Создаем QStackedWidget

        # Добавляем страницы в QStackedWidget
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        # Добавляем контент на страницы
        self.page1_layout = QVBoxLayout()
        self.page1_layout.addWidget(QPushButton('Page 1'))
        self.page1.setLayout(self.page1_layout)

        self.page2_layout = QVBoxLayout()
        self.page2_layout.addWidget(QPushButton('Page 2'))
        self.page2.setLayout(self.page2_layout)

        # Создаем кнопки для переключения страниц
        self.btn1 = QPushButton('Go to Page 1')
        self.btn2 = QPushButton('Go to Page 2')

        self.btn1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn2.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        # Создаем основной макет
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stack)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.btn1)
        self.btn_layout.addWidget(self.btn2)

        self.layout.addLayout(self.btn_layout)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec())