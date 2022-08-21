from curses import color_content
import tkinter


def contenido(x):

    ventana = tkinter.Tk()
    ventana.geometry("400x300")

    etiqueta = tkinter.Label(ventana, text=x)
    etiqueta.pack()

    cajaTexto = tkinter.Entry(ventana)
    cajaTexto.pack()

    def imprimir():
        etiqueta2 = tkinter.Label(ventana, text=cajaTexto.get())
        etiqueta2.pack()
        
    boton = tkinter.Button(ventana, text="Imprimir", command=imprimir)
    boton.pack()

    ventana.mainloop()
