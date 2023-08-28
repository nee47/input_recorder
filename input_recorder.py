import keyboard
import time
import threading

# x, y = pa.position()
# combinacion_teclas = 'ctrl+1'

# print(f"Posición actual del mouse: ({x}, {y})")

# def my_function():
#     print("Se presionó la combinación Ctrl + 1")

# # Agregar la combinación de teclas Ctrl + 1
# keyboard.add_hotkey(combinacion_teclas, my_function)

# keyboard.wait("esc")

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
        import pyautogui as pa
        for coordinate in self.coordinates:
            pa.moveTo(coordinate[0], coordinate[1])
            #time.sleep(0.1)
    
    def _store_coordinates(self):
        import pyautogui as pa 
        
        while not self.stop_event.is_set():
            point = pa.position()
            if point not in self.coordinates:
                self.coordinates.append((point.x, point.y))
            #time.sleep(0.1)

    def start_recording(self):
        self.thread = threading.Thread(target=self._store_coordinates)
        self.thread.start()

    def show_coordinates(self):
        for coordinate in self.coordinates:
            print(f"las coordenadas son ({coordinate[0]}, {coordinate[1]})")
        print(f"la cantidad de coordenadas almacenadas fueron: {len(self.coordinates)}")

    def stop_recording(self):
        self.stop_event.set()
        self.thread.join()
