import keyboard
import pyautogui as pa 


x, y = pa.position()
combinacion_teclas = 'ctrl+1'

print(f"Posición actual del mouse: ({x}, {y})")

def my_function():
    print("Se presionó la combinación Ctrl + 1")

# Agregar la combinación de teclas Ctrl + 1
keyboard.add_hotkey(combinacion_teclas, my_function)

keyboard.wait("esc")

import tkinter as tk

def button1_click():
    label.config(text="Botón 1 fue presionado")

def button2_click():
    label.config(text="Botón 2 fue presionado")
   

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Botones")

# Crear etiqueta para mostrar mensajes
label = tk.Label(root, text="")
label.pack()

# Crear botones
button1 = tk.Button(root, text="Botón 1", command=button1_click)
button1.pack()

button2 = tk.Button(root, text="Botón 2", command=button2_click)
button2.pack()

# Iniciar el bucle de eventos
root.mainloop()