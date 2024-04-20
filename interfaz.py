import PySimpleGUI as sg
import os.path

#sg.Window(title="Prueba")

nombre = "Ramiro Carmona"

edad = "22 años"

escuela = "BUAP"

informacionPersonal = [
    [sg.Text(nombre)],
    [sg.Text(edad)],
    [sg.Text(escuela)],
    [sg.Button("Salir")]
]

visualizadorImagen = [
    [sg.Text("Reconociendo rostro")],
    [sg.Text(size=(70,0), key="-TOUT-")],
    [sg.Image(filename="C:/Users/ydg_g/OneDrive/Imágenes/Rostros/foundry.png")]
]

layout = [
    [sg.Column(informacionPersonal),
     sg.VSeparator(),
     sg.Column(visualizadorImagen)]
]

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == "Salir" or event == sg.WINDOW_CLOSED:
        break

