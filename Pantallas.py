"""
En este documento se trabajaran todas las pantallas que vamos a utilizar
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Página de Inicio", font=("Helvetica", 18))
        label.pack(pady=25)

class PillPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Crear el canvas para el rectángulo
        canvas = tk.Canvas(self, width=360, height=640)  # Tamaño total del canvas
        canvas.pack()

        # Dibujar el rectángulo en la parte superior (100 px de alto, 360 px de largo)
        rect_x1 = 0
        rect_y1 = 0
        rect_x2 = 360
        rect_y2 = 100
        canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill="white", outline="black")

        # Crear la etiqueta de título y superponerla sobre el rectángulo superior
        label = tk.Label(self, text="MI PASTILLA", font=("Helvetica", 18), bg="white")
        label.place(x=180, y=50, anchor="center")  # Posición centrada en el rectángulo superior

        # Cargar y colocar imágenes en las esquinas superiores
        self.add_images(canvas)

        # Coordenadas del segundo rectángulo
        rect_x1_2 = 30
        rect_y1_2 = 125
        rect_x2_2 = 330
        rect_y2_2 = 240
        radius = 20  # Radio para las esquinas redondeadas

        # Dibujar rectángulo con bordes ovalados
        self.create_rounded_rectangle(canvas, rect_x1_2, rect_y1_2, rect_x2_2, rect_y2_2, radius, fill="white", outline="black")

        # Definir variables para los textos de medicamentos y horarios
        self.med_1 = "LORATADINA"
        self.time_1 = "10:00 AM"
        self.med_2 = "PARACETAMOL"
        self.time_2 = "3:00 PM"
        self.med_3 = "ANOXION"
        self.time_3 = "6:00 PM"
        self.med_4 = "PEPTOBISMOL"
        self.time_4 = "10:00 PM"

        # Crear la primera etiqueta dentro del segundo rectángulo (arriba a la izquierda)
        label_1_2 = tk.Label(self, text="PRÓXIMA PASTILLA", font=("Helvetica", 16), bg="white")
        label_1_2.place(x=rect_x1_2 + 10, y=rect_y1_2 + 10)  # Un poco alejado de la esquina

        # Crear la segunda etiqueta dentro del segundo rectángulo (centrada)
        label_2_2 = tk.Label(self, text=f"{self.med_1} {self.time_1}", font=("Helvetica", 12), bg="white")
        label_2_2.place(x=(rect_x1_2 + rect_x2_2) // 2, y=(rect_y1_2 + rect_y2_2) // 2, anchor="center")

        # Coordenadas del tercer rectángulo
        rect_x1_3 = 30
        rect_y1_3 = 260
        rect_x2_3 = 330
        rect_y2_3 = 340
        radius = 20  # Radio para las esquinas redondeadas

        # Dibujar el tercer rectángulo con bordes ovalados
        self.create_rounded_rectangle(canvas, rect_x1_3, rect_y1_3, rect_x2_3, rect_y2_3, radius, fill="white", outline="black")

        # Crear la primera etiqueta dentro del tercer rectángulo (izquierda)
        label_1_3 = tk.Label(self, text=self.med_2, font=("Helvetica", 16), bg="white")
        label_1_3.place(x=rect_x1_3 + 10, y=(rect_y1_3 + rect_y2_3) // 2, anchor="w")  # Alineado a la izquierda

        # Crear la segunda etiqueta dentro del tercer rectángulo (derecha)
        label_2_3 = tk.Label(self, text=self.time_2, font=("Helvetica", 12), bg="white")
        label_2_3.place(x=rect_x2_3 - 10, y=(rect_y1_3 + rect_y2_3) // 2, anchor="e")  # Alineado a la derecha
        
        # Coordenadas del cuarto rectángulo
        rect_x1_4 = 30
        rect_y1_4 = 360
        rect_x2_4 = 330
        rect_y2_4 = 440
        radius = 20  # Radio para las esquinas redondeadas

        # Dibujar el cuarto rectángulo con bordes ovalados
        self.create_rounded_rectangle(canvas, rect_x1_4, rect_y1_4, rect_x2_4, rect_y2_4, radius, fill="white", outline="black")

        # Crear la primera etiqueta dentro del cuarto rectángulo (izquierda)
        label_1_4 = tk.Label(self, text=self.med_3, font=("Helvetica", 16), bg="white")
        label_1_4.place(x=rect_x1_4 + 10, y=(rect_y1_4 + rect_y2_4) // 2, anchor="w")  # Alineado a la izquierda

        # Crear la segunda etiqueta dentro del cuarto rectángulo (derecha)
        label_2_4 = tk.Label(self, text=self.time_3, font=("Helvetica", 12), bg="white")
        label_2_4.place(x=rect_x2_4 - 10, y=(rect_y1_4 + rect_y2_4) // 2, anchor="e")  # Alineado a la derecha

        # Coordenadas del quinto rectángulo
        rect_x1_5 = 30
        rect_y1_5 = 460
        rect_x2_5 = 330
        rect_y2_5 = 540
        radius = 20  # Radio para las esquinas redondeadas

        # Dibujar el quinto rectángulo con bordes ovalados
        self.create_rounded_rectangle(canvas, rect_x1_5, rect_y1_5, rect_x2_5, rect_y2_5, radius, fill="white", outline="black")

        # Crear la primera etiqueta dentro del quinto rectángulo (izquierda)
        label_1_5 = tk.Label(self, text=self.med_4, font=("Helvetica", 16), bg="white")
        label_1_5.place(x=rect_x1_5 + 10, y=(rect_y1_5 + rect_y2_5) // 2, anchor="w")  # Alineado a la izquierda

        # Crear la segunda etiqueta dentro del quinto rectángulo (derecha)
        label_2_5 = tk.Label(self, text=self.time_4, font=("Helvetica", 12), bg="white")
        label_2_5.place(x=rect_x2_5 - 10, y=(rect_y1_5 + rect_y2_5) // 2, anchor="e")  # Alineado a la derecha

        # Dibujar el rectángulo en la parte inferior (100 px de alto, 360 px de largo)
        rect_y1_6 = 580  # Comenzar 100 píxeles antes del final
        rect_y2_6 = 640  # Termina en el final del canvas
        canvas.create_rectangle(rect_x1, rect_y1_6, rect_x2, rect_y2_6, fill="white", outline="black")

        # Colocar imágenes en el rectángulo inferior
        self.add_images_to_bottom(canvas)

    def add_images(self, canvas):
        # Cargar las imágenes
        img1 = Image.open(r"C:\Users\obedc\OneDrive\Documentos\IPN\IHM\telefono.png")
        img1 = img1.resize((75, 75), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.img1_tk = ImageTk.PhotoImage(img1)
        canvas.create_image(20, 20, anchor="nw", image=self.img1_tk)  # Imagen en la parte superior izquierda

        img2 = Image.open(r"C:\Users\obedc\OneDrive\Documentos\IPN\IHM\telefono.png")  # Cambia por la ruta de tu imagen
        img2 = img2.resize((75, 75), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.img2_tk = ImageTk.PhotoImage(img2)
        canvas.create_image(340, 20, anchor="ne", image=self.img2_tk)  # Imagen en la parte superior derecha

    def add_images_to_bottom(self, canvas):
        # Cargar imágenes diferentes para la parte inferior
        img3 = Image.open(r"C:\Users\obedc\OneDrive\Documentos\IPN\IHM\AddLogo.png")
        img3 = img3.resize((30, 30), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.img3_tk = ImageTk.PhotoImage(img3)
        canvas.create_image(70, 625, anchor="s", image=self.img3_tk)  # Imagen en la parte inferior izquierda

        img4 = Image.open(r"C:\Users\obedc\OneDrive\Documentos\IPN\IHM\HomeLogo.png")
        img4 = img4.resize((30, 30), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.img4_tk = ImageTk.PhotoImage(img4)
        canvas.create_image(180, 625, anchor="s", image=self.img4_tk)  # Imagen en el centro

        img5 = Image.open(r"C:\Users\obedc\OneDrive\Documentos\IPN\IHM\PillLogo.png")
        img5 = img5.resize((30, 30), Image.LANCZOS)  # Redimensionar la imagen si es necesario
        self.img5_tk = ImageTk.PhotoImage(img5)
        canvas.create_image(290, 625, anchor="s", image=self.img5_tk)  # Imagen en la parte inferior derecha

    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        # Crear un rectángulo redondeado utilizando un polígono
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]
        return canvas.create_polygon(points, smooth=True, **kwargs)

    # Método para crear las etiquetas de medicamentos (puedes modificar este método si deseas agregar más)
    def create_medicines(self, canvas):
        # Implementar la creación de otros rectángulos y etiquetas
        pass  # Aquí puedes agregar el código para otros rectángulos similares a los anteriores

# Función principal
def main():
    root = tk.Tk()
    root.title("Pastillero Inteligente")  # Título de la ventana
    root.geometry("360x640")  # Tamaño de la ventana

    app = PillPage(root, None)
    app.pack(fill="both", expand=True)
    
    root.mainloop()  # Iniciar el bucle de eventos

if __name__ == "__main__":
    main()


class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Página para gregar pastilla", font=("Helvetica", 18))
        label.pack(pady=25)

class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Página Para Perfil", font=("Helvetica", 18))
        label.pack(pady=25)

class NotificationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Página recibir notificaciones", font=("Helvetica", 18))
        label.pack(pady=25)
