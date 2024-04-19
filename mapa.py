import tkinter
from tkintermapview import TkinterMapView

# Crear la ventana de tkinter
root_tk = tkinter.Tk()
root_tk.geometry("800x600")
root_tk.title("Mapa de Riesgo")

# Crear el widget del mapa
map_widget = TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Establecer la posición y el zoom del mapa
map_widget.set_position(19.0414, -98.2063)  # Ciudad de Puebla
map_widget.set_zoom(15)

# Función para agregar un marcador cuando se hace clic con el botón derecho
def add_marker(event):
    # Convertir las coordenadas del ratón a latitud y longitud
    lat, lon = map_widget.canvas_to_latlon(event.x, event.y)

    # Agregar un marcador en la posición del ratón
    map_widget.add_marker(lat, lon)

# Vincular el evento del botón derecho del ratón a la función add_marker
map_widget.bind("<Button-3>", add_marker)

# Iniciar el bucle principal de tkinter
root_tk.mainloop()
