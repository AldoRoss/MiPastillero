import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from Pantallas import HomePage, PillPage, AddPage, UserPage, NotificationPage

class MobileApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.title("Mi Pastillero")
        self.geometry("380x762")
        # Cargar la imagen del logo
        self.logo = tk.PhotoImage(file="ElementosGraficos\logo.png")
        self.iconphoto(False,self.logo)

        self.create_top_bar()
        
        # Contenedor principal para las pantallas
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (HomePage, PillPage, AddPage, UserPage, NotificationPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # Coloca todas las pantallas en el mismo lugar
            frame.grid(row=0, column=0, sticky="nsew")
    

        self.show_frame("HomePage")
        
        # Crear la barra de navegación inferior
        self.create_bottom_nav()
        
        # Crear estilo para botones
        style = ttk.Style(self)
        style.configure('Custom.TButton', 
                        font=('Helvetica', 12, 'bold'),  # Cambia la fuente
                        foreground='#7c70de',              # Color del texto
                        background='#2e86c1',            # Color de fondo
                        padding=10,                      # Relleno interno del botón
                        borderwidth=2                    # Grosor del borde
                        )

        # Si quieres cambiar el color cuando el mouse está encima (hover)
        style.map('Custom.TButton',
                  background=[('active', '#FFFFFF')],  # Color al pasar el mouse
                  foreground=[('active', '#FFFFFF')])

    def show_frame(self, page_name):
        """Muestra una pantalla en base al nombre"""
        frame = self.frames[page_name]
        frame.tkraise()

    def create_top_bar(self):
        # Frame para la barra superior
        top_bar = tk.Frame(self, bg="#FFFFFF", height=100)
        top_bar.pack(side="top", fill="x")

        # Botón de la izquierda 
        left_button = ttk.Button(top_bar, text="Menú", command=lambda: self.show_frame("NotificationPage"))
        left_button.pack(side="right", padx=10)

        # Cargar imagen del usuario y convertirla en un círculo
        user_img = Image.open("ElementosGraficos\logo.png")
        user_img_resized = user_img.resize((60, 60)) 

        # Crear una máscara circular
        mask = Image.new('L', (60, 60), 0)  # Crear imagen negra (0 es completamente negro)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 60, 60), fill=255)  # Dibujar un círculo blanco (255 es completamente blanco)

        # Aplicar la máscara a la imagen redimensionada
        user_img_circular = Image.new("RGBA", user_img_resized.size)
        user_img_circular.paste(user_img_resized, (0, 0), mask=mask)

        # Convertir a un formato compatible con Tkinter
        user_img_tk = ImageTk.PhotoImage(user_img_circular)

        # Botón de la derecha con la foto circular del usuario
        right_button = ttk.Button(top_bar, image=user_img_tk, command=lambda: self.show_frame("UserPage"))
        right_button.image = user_img_tk  # Para evitar que se elimine la referencia a la imagen
        right_button.pack(side="left", padx=10)


    def create_bottom_nav(self):
        """Crear la barra de navegación inferior con 3 botones"""
        nav_frame = tk.Frame(self, bg="#FFFFFF", height=50)
        nav_frame.pack(side="bottom", fill = "x")

        # Botón de Inicio
        self.img = Image.open("ElementosGraficos\homeLogo.png")
        self.img_resized = self.img.resize((50, 50))  # Redimensionar la imagen si es necesario
        self.img_home = ImageTk.PhotoImage(self.img_resized)

        #Declarar boton
        home_button = ttk.Button(nav_frame, image=self.img_home,
                                 style='Custom.TButton',
                                 command=lambda: self.show_frame("HomePage"))
        home_button.pack(side="left", expand=True)

        # Botón de Pastillas
        self.img = Image.open("ElementosGraficos\pillLogo.png")
        self.img_resized = self.img.resize((50, 50))  # Redimensionar la imagen si es necesario
        self.img_pill = ImageTk.PhotoImage(self.img_resized)

        pill_button = ttk.Button(nav_frame, image=self.img_pill,
                                 style='Custom.TButton',
                                 command=lambda: self.show_frame("PillPage"))
        pill_button.pack(side="left", expand=True)

        # Botón de Configuración
        self.img = Image.open("ElementosGraficos\AddLogo.png")
        self.img_resized = self.img.resize((50, 50))  # Redimensionar la imagen si es necesario
        self.img_add = ImageTk.PhotoImage(self.img_resized)
        settings_button = ttk.Button(nav_frame,image=self.img_add, 
                                     style='Custom.TButton',
                                     command=lambda: self.show_frame("AddPage"))
        settings_button.pack(side="left", expand=True)

    def left_button_action(self):
        print("Menú presionado")

    def right_button_action(self):
        print("Foto del usuario presionada")



if __name__ == "__main__":
    app = MobileApp()
    app.mainloop()
