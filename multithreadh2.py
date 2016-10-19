import time
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Base init")

        self.thread = QThread()
        self.w = Worker()
        self.w.finished[int].connect(self.on_finished)
        self.w.moveToThread(self.thread)
        self.thread.started.connect(self.w.work)
        self.thread.start()

    @pyqtSlot(int)
    def on_finished(self, i):
        print("Base caught finished, {}".format(i))


class Worker(QObject):
    finished = pyqtSignal(int)

    def __init__(self):
        print("Worker init")
        super().__init__()

    def work(self):
        print("Worker work")
        time.sleep(10)
        self.finished.emit(42)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
