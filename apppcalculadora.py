from glob import glob
from tkinter import*
from math import*

ventana=Tk()
ventana.title("Calculadora basica")
ventana.geometry("400x500")
ventana.resizable(False,False)
ventana.configure(background="grey1")

color_boton="gray70"
color_boton1="DarkOrange2"
ancho_boton=10
ancho_boton1=24
alto_boton=3

operador=""
texto_pantalla= StringVar()
def clear():
    global operador
    operador= " "
    texto_pantalla.set("0")
def click(b):
    global operador
    operador += str(b)
    texto_pantalla.set(operador)
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "ERROR"
    texto_pantalla.set(r)



#borones de la primera fila
Boton_parentesis_abierto= Button(ventana,text="(",bg="gray30",width=ancho_boton,height=alto_boton,command=lambda:click("(")).grid(row=1,column=0,pady=10)
Boton_parentesis_cerrado= Button(ventana,text=")",bg="gray30",width=ancho_boton,height=alto_boton,command=lambda:click(")")).grid(row=1,column=1,pady=10)
Boton_borrar_todo= Button(ventana,text="AC",bg="red3",width=ancho_boton1,height=alto_boton,command=clear).place(x=206,y=104)
#botones de la segunda fila
Boton7= Button(ventana,text=7,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(7)).grid(row=2,column=0,pady=10)
Boton8= Button(ventana,text=8,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(8)).grid(row=2,column=1,pady=10)
Boton9= Button(ventana,text=9,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(9)).grid(row=2,column=2,pady=10)
Boton_division= Button(ventana,text="÷",bg=color_boton1,width=ancho_boton,height=alto_boton,command=lambda:click("/")).grid(row=2,column=3,pady=10)
#botones tercera fila
Boton4= Button(ventana,text=4,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(4)).grid(row=3,column=0,pady=10)
Boton5= Button(ventana,text=5,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(5)).grid(row=3,column=1,pady=10)
Boton6= Button(ventana,text=6,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(6)).grid(row=3,column=2,pady=10)
Boton_multiplicacion= Button(ventana,text="x",bg=color_boton1,width=ancho_boton,height=alto_boton,command=lambda:click("*")).grid(row=3,column=3,pady=10)
#botones cuarta fila
Boton1= Button(ventana,text=1,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(1)).grid(row=4,column=0,pady=10)
Boton2= Button(ventana,text=2,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(2)).grid(row=4,column=1,pady=10)
Boton3= Button(ventana,text=3,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(3)).grid(row=4,column=2,pady=10)
Boton_resta= Button(ventana,text="-",bg=color_boton1,width=ancho_boton,height=alto_boton,command=lambda:click("-")).grid(row=4,column=3,pady=10)
#botones quinta fila
Boton0= Button(ventana,text=0,bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(0)).grid(row=5,column=0,pady=10)
Boton_decimal= Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(".")).grid(row=5,column=1,pady=10)
Boton_igual= Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).grid(row=5,column=2,pady=10)
Boton_sumar= Button(ventana,text="+",bg=color_boton1,width=ancho_boton,height=alto_boton,command=lambda:click("+")).grid(row=5,column=3,pady=10)



Pantalla = Entry(ventana,font=("arial",20,"bold"),width=22,borderwidth=10,background="snow",textvariable=texto_pantalla)
Pantalla.grid(row=0,column=0,columnspan=4,padx=20,pady=20)
ventana.mainloop()