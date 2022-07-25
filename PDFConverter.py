from dis import Instruction
from fileinput import filename
import tkinter as tk
from turtle import title, width
import PyPDF2
from PIL import Image, ImageTk
from tkinter import PhotoImage, filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image
from tkinter.filedialog import askopenfile, askopenfilename
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from tkinter.simpledialog import askstring

root = tk.Tk()
root.title("PDFconverter")

Canvas = tk.Canvas(root, width=620, height=300)
Canvas.grid(columnspan=3, rowspan=5)

#window icon
photo = PhotoImage(file="icono.png")
root.iconphoto(False, photo)

#logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#label con texto
instruction = tk.Label(root, text="Select an image to convert to PDF.", font= "Raleway-Regular",bg="#f0f0f0")
instruction.config(fg="#552721")
instruction.grid(columnspan=3, column=0, row=1)

#acción de buscar el archivo
def select_file():
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt')
        
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    #texto mostrando el nombre y la dirección del archivo
    instruction1 = tk.Label(root, text=filename, font="Raleway-Regular")
    instruction1.grid(columnspan=3, column=0, row=3)

    #dialogo para guardar la imagen en pdf con el usuario eligiendo el nombre
    guardado = tk.simpledialog.askstring("Save", "Enter save name:", )
    image1 = Image.open(filename)
    img1 = image1.convert('RGB')
    img1.save(guardado+".pdf")

#boton buscar
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway-Regular", bg="#c23f2e", fg="white", height=2, width=15, relief="flat", command =lambda:select_file())
browse_text.set("Browse")
browse_btn.grid(column= 1, row=2) 

Canvas = tk.Canvas(root, width=20, height=30)
Canvas.grid(columnspan=3, rowspan=3)



root.mainloop()