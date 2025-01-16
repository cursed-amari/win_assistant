from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox, QProgressBar, QFrame
from PyQt6 import QtWidgets, QtCore
import subprocess
import pkg_resources
import sys


def check_and_update_pytubefix():
    package_name = "pytubefix"

    try:
        # Получаем установленную версию
        installed_version = pkg_resources.get_distribution(package_name).version
        print(f"Текущая версия {package_name}: {installed_version}")

        # Выполняем обновление через pip
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Проверяем вывод на наличие обновления
        if "Requirement already satisfied" in result.stdout:
            print(f"{package_name} уже обновлён.")
        else:
            print(f"{package_name} обновлён до последней версии.")
            print(result.stdout)

    except pkg_resources.DistributionNotFound:
        print(f"{package_name} не установлен. Устанавливаем...")
        subprocess.run([sys.executable, "-m", "pip", "install", package_name])


# Запускаем проверку и обновление pytubefix
check_and_update_pytubefix()

# Импортируем библиотеку после проверки
from pytubefix import YouTube

class PageDownloaderInit:
    def __init__(self):
        self.page_downloader = QtWidgets.QWidget()
        self.page_downloader.setObjectName("page_downloader")
        self.verticalLayout_frame = QtWidgets.QVBoxLayout(self.page_downloader)
        self.verticalLayout_frame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_frame.setSpacing(0)
        self.verticalLayout_frame.setObjectName("verticalLayout_frame")

        # Строка ввода для ссылки
        self.url_label = QLabel('YouTube Video URL:')
        self.url_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.verticalLayout_frame.addWidget(self.url_label)

        self.frame_spacer = QFrame()
        self.verticalLayout_frame.addWidget(self.frame_spacer)

        self.url_input = QLineEdit()
        self.verticalLayout_frame.addWidget(self.url_input)

        # Чекбокс для выбора скачивания только аудио
        self.audio_only_checkbox = QCheckBox(text='Скачать только аудио')
        self.verticalLayout_frame.addWidget(self.audio_only_checkbox)

        # Прогресс бар
        self.progress_bar = QProgressBar()
        self.verticalLayout_frame.addWidget(self.progress_bar)

        # Кнопка для скачивания
        self.download_button = QPushButton('Скачать')
        self.download_button.clicked.connect(self.download_video)
        self.verticalLayout_frame.addWidget(self.download_button)

    def get_widget(self):
        return self.page_downloader

    def download_video(self):
        url = self.url_input.text()
        audio_only = self.audio_only_checkbox.isChecked()

        if not url:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите ссылку на видео.")
            return

        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)

            if audio_only:
                # Используем get_audio_only() для получения аудиопотока
                stream = yt.streams.get_audio_only()
                if stream:
                    stream.download(filename=f"{yt.title}.mp3")
                else:
                    # QMessageBox.critical(self, "Ошибка", "Не удалось найти аудиопоток.")
                    return
            else:
                # Получаем видео в самом высоком разрешении
                stream = yt.streams.get_highest_resolution()
                if stream:
                    stream.download()
                else:
                    # QMessageBox.critical(self, "Ошибка", "Не удалось найти видеопоток.")
                    return

            # QMessageBox.information(self, "Успех", "Скачивание завершено!")
            self.progress_bar.setValue(0)  # Сбросить прогресс бар после завершения
        except Exception as e:
            print(e)
            # QMessageBox.critical(self, "Ошибка", f"Не удалось скачать видео: {str(e)}")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = int(bytes_downloaded / total_size * 100)
        self.progress_bar.setValue(percentage)