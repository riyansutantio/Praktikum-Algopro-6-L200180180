from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Kalkulator')

L1 = Label (my_app, text = 'Angka 1 : ')
L1.grid(row=0, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(columnspan=3 ,row=0, column=1)

L2 = Label (my_app, text = 'Angka 2 : ')
L2.grid(row=1, column=0)
str2 = StringVar()
E2 = Entry(my_app, textvariable=str2)
E2.grid(columnspan=3 ,row=1, column=1)

def tambah():
    p=float(str1.get())
    q=float(str2.get())
    r=p+q
    L.config(text=r)

def kurang():
    p=float(str1.get())
    q=float(str2.get())
    r=p-q
    L.config(text=r)

def kali():
    p=float(str1.get())
    q=float(str2.get())
    r=p*q
    L.config(text=r)

def bagi():
    p=float(str1.get())
    q=float(str2.get())
    r=p/q
    L.config(text=r)

B1 = Button(my_app, text='+', command= tambah)
B1.grid(row=2, column=0)

B2 = Button(my_app, text='-', command= kurang)
B2.grid(row=2, column=1)

B3 = Button(my_app, text='*', command= kali)
B3.grid(row=2, column=2)

B4 = Button(my_app, text='/', command= bagi)
B4.grid(row=2, column=3)

L3 = Label(my_app, text='Hasil')
L3.grid(row=3, column= 0)

L = Label(my_app, text='0')
L.grid(row=3, column= 1)

my_app.mainloop()




    
