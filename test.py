from PySide6 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets, QtMultimedia
from PySide6.QtGui import QKeyEvent, QMouseEvent, QPalette, QResizeEvent
from PySide6.QtCore import Qt


class VideoWidget(QtMultimediaWidgets.QVideoWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored)

        p = self.palette()
        p.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.black)
        self.setPalette(p)

    def keyPressEvent(self, event: QKeyEvent):
        if (event.key() == QtCore.Qt.Key.Key_Escape or event.key() == QtCore.Qt.Key.Key_Back) and self.isFullScreen():
            self.setFullScreen(False)
            event.accept()
        elif event.key() == QtCore.Qt.Key.Key_F:
            self.setFullScreen(not self.isFullScreen())
            event.accept()
        else:
            super().keyPressEvent(event)

    def setFullScreen(self, fullScreen: bool):
        if self.isFullScreen() == fullScreen:
            return

        if self.isFullScreen():
            self.resize(QtCore.QSize(600, 480))
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint, False)
            self.showNormal()

        else:
            self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
            self.resize(QtCore.QSize(1920, 1080))
            self.showFullScreen()

        # super().setFullScreen(fullScreen)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.setFullScreen(not self.isFullScreen())
        event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        # TODO: Signal player to play/stop video
        super().mousePressEvent(event)

    def resizeEvent(self, event: QResizeEvent) -> None:
        print("T1", self.isFullScreen(), event.size(), self.size())
        super().resizeEvent(event)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    player = QtMultimedia.QMediaPlayer()

    videoOutput = VideoWidget()
    videoOutput.show()
    audioOutput = QtMultimedia.QAudioOutput()
    audioOutput.setVolume(1.0)

    player.setAudioOutput(audioOutput)
    player.setVideoOutput(videoOutput)
    player.setSource(QtCore.QUrl("1min.mp4"))

    player.play()

    print(player.bufferProgress())

    sys.exit(app.exec())
