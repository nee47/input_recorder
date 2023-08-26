import keyboard
import pyautogui as pa 
import time
import threading

x, y = pa.position()
combinacion_teclas = 'ctrl+1'

print(f"Posición actual del mouse: ({x}, {y})")

def my_function():
    print("Se presionó la combinación Ctrl + 1")

# Agregar la combinación de teclas Ctrl + 1
keyboard.add_hotkey(combinacion_teclas, my_function)

keyboard.wait("esc")

class InputRecorder():
    def __init__(self):
        self.recording = False
        self.playing = False
        self.coordinates = []
        self.stop_event = threading.Event()
        self.thread = None

    def stop(self):
        pass

    def play(self):
        pass

    def _store_coordinates(self):
        while not self.stop_event.is_set():
            self.coordinates.append(pa.position())
            time.sleep(0.1)

    def start_recording(self):
        self.thread = threading.Thread(target=self._store_coordinates)
        self.thread.start()

    def show_coordinates(self):
        print(self.coordinates)

    def stop_recording(self):
        self.stop_event.set()
        self.thread.join()