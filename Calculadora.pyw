# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:07:04 2020

@author: Ing Cris Rios
"""

from tkinter import *
######################################################## RAIZ Y EL FRAME

raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

########################### PANTALLA EN EL FRAME

numeroPantalla = StringVar()
pantalla = Entry(miFrame)
pantalla.grid(row = 1, column = 1 ,padx = 10 , pady =10, columnspan = 4) #FUNCION COLSPAN(colspan--)  parar trabajar con tablas
pantalla.config(background = "black", fg="green2", justify ="right")

############################# PULSACIONES TECLADO

def numeroPulsado(num):
    
    numeroPantalla.set(numeroPantalla.get() + num)
    


########################### FILA 1 --- FUNCION COLSPAN(colspan--) columnspan = 4 arriba me organiza las columbas

boton7 = Button(miFrame, text = "7", width = 3)
boton7.grid(row =2, column = 1)
boton8 = Button(miFrame, text = "8", width = 3)
boton8.grid(row =2, column = 2)
boton9 = Button(miFrame, text = "9", width = 3)
boton9.grid(row =2, column = 3)
botonMult = Button(miFrame, text = "x", width = 3)
botonMult.grid(row =2, column = 4)

########################################### Fila 2

boton4 = Button(miFrame, text = "4", width = 3 , command = lambda:numeroPulsado("4"))
boton4.grid(row =3, column = 1)
boton5 = Button(miFrame, text = "5", width = 3)
boton5.grid(row =3, column = 2)
boton6 = Button(miFrame, text = "6", width = 3)
boton6.grid(row =3, column = 3)
botonDiv = Button(miFrame, text = "/", width = 3)
botonDiv.grid(row =3, column = 4)

###################################### Fila 3

boton1 = Button(miFrame, text = "1", width = 3)
boton1.grid(row =4, column = 1)
boton2 = Button(miFrame, text = "2", width = 3)
boton2.grid(row =4, column = 2)
boton3 = Button(miFrame, text = "3", width = 3)
boton3.grid(row =4, column = 3)
botonRest = Button(miFrame, text = "-", width = 3)
botonRest.grid(row =4, column = 4)

######################################Fila 4

boton0 = Button(miFrame, text = "0", width = 3)
boton0.grid(row =5, column = 1)
botonComa = Button(miFrame, text = ",", width = 3)
botonComa.grid(row =5, column = 2)
botonIgual = Button(miFrame, text = "=", width = 3)
botonIgual.grid(row =5, column = 3)
botonSum = Button(miFrame, text = "+", width = 3)
botonSum.grid(row =5, column = 4)


########################################### 


raiz.mainloop()

