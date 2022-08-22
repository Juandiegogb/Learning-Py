import tkinter


def contenido():

    ventana = tkinter.Tk()
    ventana.geometry("400x300")

    Usuario = tkinter.Label(ventana, text="Usuario")
    Usuario.pack()

    cajaUsuario = tkinter.Entry(ventana)
    cajaUsuario.pack()

    Clave = tkinter.Label(ventana, text="Clave")
    Clave.pack()

    cajaClave = tkinter.Entry(ventana)
    cajaClave.pack()

    

    def login( cajaUsuario, cajaClave):
        user = "Juan"
        clave = "1234"

        print(cajaClave.get())

        if cajaUsuario.get() == user and cajaClave.get() == clave:
            print("Hola")

    boton = tkinter.Button(ventana, text="Login", command = lambda:login(cajaUsuario,cajaClave))
    boton.pack()

    ventana.mainloop()
