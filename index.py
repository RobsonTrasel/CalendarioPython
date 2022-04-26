from tkinter import *
import tkinter as tk


from PIL import Image, 
import calendar

original = tk.Tk()
original.geometry('400x300')
original.title("Calendario")


def show():
    mes = int(month.get())
    ano = int(year.get())
    output = calendar.month(ano, mes)
    cal.insert('end', output)
    
def clear():
    cal.delete(1.0, 'end')
    
def exit():
    original.destroy()


titulo = Label(original, text="Calendario Simples", font=('verdana', '18','bold'))
titulo.place(x=40, y=10)

m_label = Label(original,text="Mês",font=('verdana','10','bold'))
m_label.place(x=70,y=80)

month = Spinbox(original, from_= 1, to = 12,width="5") 
month.place(x=140,y=80) 
  
y_label = Label(original,text="Ano",font=('verdana','10','bold'))
y_label.place(x=210,y=80)

year = Spinbox(original, from_= 2020, to = 3000,width="8") 
year.place(x=260,y=80) 


cal = Text(original,width=33,height=8,relief=RIDGE,borderwidth=2)
cal.place(x=70,y=110)

show = Button(original,text="Mostrar",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=2,command=show)
show.place(x=140,y=250)

clear = Button(original,text="Limpar",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=2,command=clear)
clear.place(x=200,y=250)

exit = Button(original,text="Sair",font=('verdana',10,'bold'),relief=RIDGE,borderwidth=2,command=exit)
exit.place(x=260,y=250)
original.mainloop()