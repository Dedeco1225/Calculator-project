#importing tkinter
from cProfile import label
from codecs import BOM_UTF32
from pickle import FRAME
from tkinter import *
from tkinter import ttk
from tokenize import String
from turtle import width

from matplotlib.backend_bases import button_press_handler
from matplotlib.pyplot import text
from numpy import place
from regex import B

# color
cor1 = "#2b2b2a" # black
cor2 = "#f0f2f5" # white
cor3 = "#052b63" # blue
cor4 = "#c3cad4" # grey
cor5 = "#db5209" # orange



janela =Tk()
janela.title("Calculadora")
janela.geometry("234x310")
janela.config(bg=cor1)

# creating Frame
frame_tela = Frame(janela, width=234, height=49, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=234, height=268)
frame_body.grid(row=1, column=0)


# variável todos Valores
todos_valores = ''

#Creating Label
valor_texto = StringVar()

#creating function

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #passando valor para tela
    valor_texto.set(todos_valores)

#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#Função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")




#Creating Label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18' ),bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


# creating buttons
b_1 = Button(frame_body, command=limpar_tela,text="C", width=11, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_body, command= lambda: entrar_valores('%'), text="%", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_body, command= lambda: entrar_valores('/'), text="/", width=5, height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_body, command= lambda: entrar_valores('7'),text="7", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_body, command= lambda: entrar_valores('8'),text="8", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_body, command= lambda: entrar_valores('9'),text="9", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_body, command= lambda: entrar_valores('*'),text="*", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)


b_8 = Button(frame_body, command= lambda: entrar_valores('4'),text="4", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_body, command= lambda: entrar_valores('5'),text="5", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_body, command= lambda: entrar_valores('6'),text="6", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_body, command= lambda: entrar_valores('-'),text="-", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_body, command= lambda: entrar_valores('1'),text="1", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_body, command= lambda: entrar_valores('%'),text="2", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_body, command= lambda: entrar_valores('2'),text="3", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_body, command= lambda: entrar_valores('3'),text="+", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_body, command= lambda: entrar_valores('+'),text="0", width=11, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_body, command= lambda: entrar_valores('.'),text=".", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_body, command= calcular, text="=", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)




janela.mainloop()












