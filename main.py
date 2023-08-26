import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import *
#from input_recorder import InputRecorder

class InputRecorderBE(QObject):
    def __init__(self):
        QObject.__init__(self)
        #self.ir = InputRecorder()

    @Slot(bool)
    def play(self, isPlaying):
        if(isPlaying):
            self.ir.stop()
        else:
            self.ir.play()

    @Slot(bool)
    def record(self, isRecording):
        if(isRecording):
            self.ir.stop_recording()
        else:
            self.ir.start_recording()
        


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    #thebackend = InputRecorderBE()
    #engine.rootContext().setContextProperty("backend", thebackend)
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())