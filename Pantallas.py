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
        label = tk.Label(self, text="Página de Pastillas", font=("Helvetica", 18))
        label.pack(pady=25)

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