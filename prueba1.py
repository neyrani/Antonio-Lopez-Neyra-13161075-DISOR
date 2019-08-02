import tkinter as tk
#from fibonacci2 import fibonacci
from fibo import fibonacci
#from hexadecimal 
#from binario import binario

class Aplicacion:
    fibo = fibonacci()
    #hexa = hexadecimal()
    #bina = binario()
    
    def __init__(self):
        self.fibo = fibonacci()
        #self.hexa = hexadecimal()
        #self.binario = binario()
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y Label")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")
        fibo = fibonacci()

        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()


    def incrementar(self):
        fibo = fibonacci()

        
        x = fibo.avanzar()
        print(x)
        y = fibo.numerofibonacci()
        #x = fibo.siguiente()
        self.valor=self.valor+1
       # numero = fibo.getNumeroActual()
        self.label1.config(text=y)
        #self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        


aplicacion1=Aplicacion()