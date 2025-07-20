import os
import threading

import requests
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox, QProgressBar, QFrame, QListWidget
from PyQt6 import QtWidgets, QtCore
import subprocess
import pkg_resources

import sys


def check_and_update_pytubefix():
    package_name_list = ("pytubefix", "yt_dlp")
    for package_name in package_name_list:
        try:
            installed_version = pkg_resources.get_distribution(package_name).version
            print(f"Текущая версия {package_name}: {installed_version}")

            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", package_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if "Requirement already satisfied" in result.stdout:
                print(f"{package_name} уже обновлён.")
            else:
                print(f"{package_name} обновлён до последней версии.")
                print(result.stdout)

        except pkg_resources.DistributionNotFound:
            print(f"{package_name} не установлен. Устанавливаем...")
            subprocess.run([sys.executable, "-m", "pip", "install", package_name])


check_and_update_pytubefix()

from pytubefix import YouTube
from yt_dlp import YoutubeDL


class PageDownloaderInit(QtWidgets.QWidget):
    info_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.processes = {}
        self.saved_music = {}

        self.page_downloader = QtWidgets.QWidget()
        self.page_downloader.setObjectName("page_downloader")
        self.verticalLayout_main_frame = QtWidgets.QVBoxLayout(self.page_downloader)
        self.verticalLayout_main_frame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_main_frame.setSpacing(0)
        self.verticalLayout_main_frame.setObjectName("verticalLayout_main_frame")

        # Строка ввода для ссылки
        self.url_label = QLabel('YouTube Video URL:')
        self.url_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.verticalLayout_main_frame.addWidget(self.url_label)

        self.frame_spacer = QFrame()
        self.verticalLayout_main_frame.addWidget(self.frame_spacer)

        self.url_input = QLineEdit()
        self.verticalLayout_main_frame.addWidget(self.url_input)

        # Чекбокс для выбора скачивания только аудио
        self.audio_only_checkbox = QCheckBox(text='Скачать только аудио')
        self.verticalLayout_main_frame.addWidget(self.audio_only_checkbox)

        # Прогресс бар
        self.progress_bar = QProgressBar()
        self.verticalLayout_main_frame.addWidget(self.progress_bar)

        # Кнопка для скачивания
        self.download_button = QPushButton('Скачать')
        self.download_button.clicked.connect(self.download_video)
        self.verticalLayout_main_frame.addWidget(self.download_button)

        self.stream_button = QPushButton('Воспроизвести')
        self.stream_button.clicked.connect(self.stream_audio)
        self.verticalLayout_main_frame.addWidget(self.stream_button)

        self.listWidget_music = QListWidget()
        self.verticalLayout_main_frame.addWidget(self.listWidget_music)
        self.listWidget_music.doubleClicked.connect(lambda event: print("click"))

        self.frame_music_navigate = QtWidgets.QFrame()
        self.verticalLayout_main_frame.addWidget(self.frame_music_navigate)
        self.layout_music_navigate = QtWidgets.QHBoxLayout()
        self.layout_music_navigate.setContentsMargins(0, 0, 0, 0)
        self.frame_music_navigate.setLayout(self.layout_music_navigate)
        self.pushButton_add_music = QtWidgets.QPushButton("+")
        self.layout_music_navigate.addWidget(self.pushButton_add_music)
        self.pushButton_add_music.clicked.connect(self.save_music)
        self.pushButton_del_music = QtWidgets.QPushButton("-")
        self.layout_music_navigate.addWidget(self.pushButton_del_music)
        self.frame_music_navigate.setMaximumHeight(30)

        self.listWidget_music_playing = QListWidget()
        self.listWidget_music_playing.itemDoubleClicked.connect(self.stop_music)
        self.verticalLayout_main_frame.addWidget(self.listWidget_music_playing)

        self.frame_button_conteiner = QtWidgets.QFrame()
        self.frame_button_conteiner_layout = QtWidgets.QHBoxLayout(self.frame_button_conteiner)
        self.pushButton_play = QPushButton("▶")
        self.pushButton_pause = QPushButton("⏸")
        self.pushButton_stop = QPushButton("⏹")
        self.frame_button_conteiner_layout.addWidget(self.pushButton_play)
        self.frame_button_conteiner_layout.addWidget(self.pushButton_pause)
        self.frame_button_conteiner_layout.addWidget(self.pushButton_stop)
        self.verticalLayout_main_frame.addWidget(self.frame_button_conteiner)

    def get_widget(self):
        return self.page_downloader

    def download_video(self):
        url = self.url_input.text()
        audio_only = self.audio_only_checkbox.isChecked()

        if not url:
            self.info_signal.emit(f"Ошибка! Пожалуйста, введите ссылку на видео.")
            return

        try:
            yt = YouTube(url, on_progress_callback=self.on_progress)

            if audio_only:
                stream = yt.streams.get_audio_only()
                if stream:
                    self.download_button.setText("Идёт загрузка")
                    stream.download(filename=f"{yt.title}.mp3")
                else:
                    self.info_signal.emit(f"Ошибка! Не удалось найти аудиопоток.")
                    return
            else:
                stream = yt.streams.get_highest_resolution()
                if stream:
                    self.download_button.setText("Идёт загрузка")
                    stream.download()
                else:
                    self.info_signal.emit(f"Ошибка! Не удалось найти видеопоток.")
                    return

            self.info_signal.emit(f"Скачивание завершено!")
            self.download_button.setText("Скачать")
            self.progress_bar.setValue(0)
        except Exception as e:
            print(e)
            self.info_signal.emit(f"Ошибка! Не удалось скачать видео: {str(e)}")

    def save_music(self, event):
        ...

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = int(bytes_downloaded / total_size * 100)
        self.progress_bar.setValue(percentage)

    def stream_audio(self):
        def play_stream(title, path):
            try:
                process = subprocess.Popen(
                    ["./ffmpeg/bin/ffplay.exe", '-nodisp', '-autoexit', path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                self.processes[title] = process
                self.listWidget_music_playing.addItem(title)
                self.info_signal.emit(f"Воспроизведение '{title}' начато.")
            except Exception as e:
                self.info_signal.emit(f"Ошибка: {str(e)}")

        url = self.url_input.text().strip()
        url = url.replace('\"', "")
        if not url:
            self.info_signal.emit("Ошибка! Введите ссылку или путь к файлу.")
            return

        file_path = os.path.abspath(url)
        if os.path.isfile(file_path):
            title = os.path.basename(file_path)
            threading.Thread(target=lambda: play_stream(title, file_path), daemon=True).start()
        else:
            try:
                with YoutubeDL({'format': 'bestaudio', 'quiet': True}) as ydl:
                    info = ydl.extract_info(url, download=False)
                    audio_url = info['url']
                    title = info.get('title', 'Без названия')
                threading.Thread(target=lambda: play_stream(title, audio_url), daemon=True).start()

            except Exception as e:
                self.info_signal.emit(f"Ошибка обработки URL: {str(e)}")

    def stop_music(self, item):
        title = item.text()

        if title in self.processes:
            process = self.processes[title]
            if process.poll() is None:
                process.terminate()
                self.info_signal.emit(f"Музыка '{title}' остановлена.")
            else:
                self.info_signal.emit(f"Ошибка! Музыка уже остановлена.")
            del self.processes[title]
        else:
            self.info_signal.emit(f"Ошибка! Процесс не найден.")

        self.listWidget_music_playing.takeItem(self.listWidget_music_playing.row(item))
