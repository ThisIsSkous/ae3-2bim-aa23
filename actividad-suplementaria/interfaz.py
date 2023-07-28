import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Mensaje", "¡Hola, has hecho clic en el botón!")

ventana = tk.Tk()
ventana.title("Interfaz")

def cerrar_ventana():
    if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
        ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

boton = tk.Button(ventana, text="Haz clic aquí", command=on_button_click)
boton.pack(pady=20)

ventana.mainloop()
