from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets, QtMultimedia
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPalette, QResizeEvent
from PyQt5.QtCore import Qt


class VideoWidget(QtMultimediaWidgets.QVideoWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)

        # p = self.palette()
        # p.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.black)
        # self.setPalette(p)

    def keyPressEvent(self, event: QKeyEvent):
        if (event.key() == QtCore.Qt.Key.Key_Escape or event.key() == QtCore.Qt.Key.Key_Back) and self.isFullScreen():
            self.setFullScreen(False)
            event.accept()
        elif event.key() == QtCore.Qt.Key.Key_F:
            self.setFullScreen(not self.isFullScreen())
            event.accept()
        else:
            super().keyPressEvent(event)

        super().keyPressEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.setFullScreen(not self.isFullScreen())
        event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        # TODO: Signal player to play/stop video
        super().mousePressEvent(event)

    # def resizeEvent(self, event: QResizeEvent) -> None:
    #     print("T1", event.size(), self.size())
    #     # self.resize(event.size())

    #     if self.isFullScreen():
    #         # self.window().resize(QtCore.QSize(1920, 1080))
    #         self.resize(QtCore.QSize(1920, 1080))
    #     else:
    #         # self.window().resize(QtCore.QSize(640, 480))
    #         self.resize(event.size())

    #     print("T2", event.size(), self.size())

    #     super().resizeEvent(event)
    #     # super().resizeEvent(event)

    #     # event.accept()


# class Template(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.subtitle_changed = QtCore.pyqtSignal(str)

#         self.setWindowTitle("app")
#         self.resize(1024, 768)

#         self.init_ui()

#     def init_ui(self):
#         main_layout = QtWidgets.QVBoxLayout()
#         tab_widget = ProjectTab()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    player = QtMultimedia.QMediaPlayer()

    video = VideoWidget()
    video.resize(800, 480)

    player.setVideoOutput(video)
    player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("1min.avi")))

    # audioOutput = QtMultimedia.QAudioOutput()
    # audioOutput.setVolume(1.0)
    # player.setAudioOutput(audioOutput)

    video.show()
    player.play()

    sys.exit(app.exec())
