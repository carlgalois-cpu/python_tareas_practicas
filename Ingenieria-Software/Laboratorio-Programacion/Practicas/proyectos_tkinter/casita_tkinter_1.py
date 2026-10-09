import tkinter as tk

class AppCasita:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Casita Interactiva")
        self.root.geometry("700x500") # Tamaño de la ventana

        # 1. El Lienzo (Canvas) para dibujar
        # Usamos un azul cielo para el fondo
        self.canvas = tk.Canvas(root, width=700, height=400, bg="#87CEEB")
        self.canvas.pack()

        # Variable para saber si es de día o de noche
        self.es_de_dia = True
        # Variable para controlar la animación
        self.animacion_activa = False

        # 2. Dibujar todos los elementos
        self.dibujar_escena()

        # 3. Crear los botones
        self.crear_controles()

    def dibujar_escena(self):
        """Dibuja todos los elementos estáticos y dinámicos en el lienzo."""
        
        # Suelo (Césped)
        self.canvas.create_rectangle(0, 350, 700, 400, fill="#228B22", outline="")

        # Sol (usamos 'tags' para poder cambiarlo después)
        self.canvas.create_oval(50, 50, 130, 130, fill="yellow", outline="orange", width=2, tags="sol")

        # Casa (Cuerpo)
        self.canvas.create_rectangle(200, 200, 500, 350, fill="white", outline="black", width=2)
        
        # Techo (Polígono)
        self.canvas.create_polygon(190, 200, 350, 100, 510, 200, fill="red", outline="black", width=2)

        # Puerta
        self.canvas.create_rectangle(240, 270, 300, 350, fill="brown", outline="black", width=2)
        # Perilla
        self.canvas.create_oval(285, 310, 295, 320, fill="gold", outline="black")

        # Ventanas rectangulares (con 'tags' para encender la luz)
        self.canvas.create_rectangle(340, 270, 400, 310, fill="white", outline="black", width=2, tags="ventana")
        self.canvas.create_rectangle(420, 270, 480, 310, fill="white", outline="black", width=2, tags="ventana")
        
        # Ventana redonda (Ático)
        self.canvas.create_oval(325, 120, 375, 170, fill="white", outline="black", width=2, tags="ventana")
        self.canvas.create_line(350, 120, 350, 170, fill="black", width=2) # Cruz vertical
        self.canvas.create_line(325, 145, 375, 145, fill="black", width=2) # Cruz horizontal
        
        # Nubes (con 'tags' para poder moverlas)
        self.canvas.create_oval(500, 60, 580, 110, fill="white", outline="", tags="nube")
        self.canvas.create_oval(540, 80, 620, 130, fill="white", outline="", tags="nube")
        self.canvas.create_oval(560, 60, 640, 110, fill="white", outline="", tags="nube")

    def crear_controles(self):
        """Crea el frame para los botones."""
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        # Botón para Día/Noche
        self.btn_dia_noche = tk.Button(control_frame, 
                                        text="Hacer de Noche 🌙", 
                                        command=self.alternar_dia_noche,
                                        font=("Arial", 12, "bold"))
        self.btn_dia_noche.pack(side=tk.LEFT, padx=10)

        # Botón para animar la nube
        self.btn_animar = tk.Button(control_frame, 
                                     text="Mover Nube ☁️", 
                                     command=self.alternar_animacion,
                                     font=("Arial", 12, "bold"))
        self.btn_animar.pack(side=tk.LEFT, padx=10)

    def alternar_dia_noche(self):
        """Cambia entre el modo día y el modo noche."""
        if self.es_de_dia:
            # Cambiar a Noche
            self.canvas.config(bg="#000033") # Cielo oscuro
            self.canvas.itemconfig("sol", fill="lightgrey", outline="grey") # Luna
            self.canvas.itemconfig("ventana", fill="yellow") # Luces encendidas
            self.btn_dia_noche.config(text="Hacer de Día ☀️")
            self.es_de_dia = False
        else:
            # Cambiar a Día
            self.canvas.config(bg="#87CEEB") # Cielo azul
            self.canvas.itemconfig("sol", fill="yellow", outline="orange") # Sol
            self.canvas.itemconfig("ventana", fill="white") # Luces apagadas
            self.btn_dia_noche.config(text="Hacer de Noche 🌙")
            self.es_de_dia = True

    def alternar_animacion(self):
        """Inicia o detiene la animación de la nube."""
        if self.animacion_activa:
            self.animacion_activa = False
            self.btn_animar.config(text="Mover Nube ☁️")
        else:
            self.animacion_activa = True
            self.btn_animar.config(text="Detener Nube 🛑")
            self.mover_nube() # Inicia el bucle de animación

    def mover_nube(self):
        """Función recursiva que mueve la nube."""
        # Si la animación debe detenerse, simplemente salimos de la función
        if not self.animacion_activa:
            return

        # Mueve todos los objetos con el tag 'nube' 2 píxeles a la derecha
        self.canvas.move("nube", 2, 0)
        
        # Obtenemos la posición de la nube
        # bbox() devuelve (x1, y1, x2, y2) de todo el grupo de nubes
        pos = self.canvas.bbox("nube")
        
        # Si la nube se sale por la derecha...
        if pos[0] > 700: # 700 es el ancho del canvas
            # La movemos de regreso al inicio, fuera de la pantalla por la izquierda
            # Calculamos el ancho de la nube (x2 - x1) y la movemos
            ancho_nube = pos[2] - pos[0]
            self.canvas.move("nube", -700 - ancho_nube, 0)

        # Le decimos a Tkinter que llame esta misma función después de 50 milisegundos
        self.root.after(50, self.mover_nube)


# --- Código principal para ejecutar la app ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AppCasita(root)
    root.mainloop()