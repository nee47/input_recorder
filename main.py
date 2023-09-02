import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import *
from input_recorder import InputRecorder, InputActions
from pynput import keyboard

class InputRecorderBE(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.actions = InputActions()
        self.ir = InputRecorder(self.actions)
        # self.t = threading.Thread(target=self._set_shortcut)
        # self.t.start()
        self.listener = None
        self._set_shortcut()
        self.isRecording = False
        self.isPlaying = False

    def on_activate_h(self):
        print('<ctrl>+1 pressed')
        self.record()

    def on_activate_i(self):
        print('<ctrl>+2 pressed')
        self.play()
        #self.listener.stop()


    def set_listener(self, hk):
        self.listener =  keyboard.GlobalHotKeys({
                hk[0]: self.on_activate_h,
                hk[1]: self.on_activate_i})
        self.listener.start()

    @staticmethod
    def keyboard_strokes_handler(key):

        # if (key == keyboard.Key.ctrl and key.char=='1'):
        #     print("hola")
        print(type(key))
        try:
            print(f"acabas de presionar : {key.char}")
            print(key)
            if(key.char == "2"):
                return False

        except AttributeError:
            print(str(key))

    def _set_shortcut(self):
        self.set_listener(("<ctrl>+1", "<ctrl>+2"))

    @Slot(bool)
    def play(self):
        
        if(self.isPlaying):
            self.ir.stop()
            self.isPlaying = False
        else:
            self.ir.play()
            self.isPlaying = True

    @Slot(bool)
    def record(self):
        
        if(self.isRecording):
            self.ir.stop_recording()
            self.ir.show_coordinates()
            # self.ir.play()
            self.isRecording = False
        else:
            self.ir.start_recording()
            self.isRecording = True
        


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    thebackend = InputRecorderBE()
    engine.rootContext().setContextProperty("backend", thebackend)
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())