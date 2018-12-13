from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Bangun Geometri')

D = Label(my_app, text ='Bangun Geometri',font='Helvetica 20 bold')
D.grid(row=0, column=0)

D1 = Label(my_app, text ='Balok adalah bangun ruang tiga dimensi ''\nyang dibentuk oleh tiga pasang persegi. ''\nBalok memiliki 6 sisi, 12 rusuk dan 8 titik sudut.',font='Helvetica 10')
D1.grid(columnspan=4,row=1, column=0)

L1 = Label (my_app, text = 'Panjang : ')
L1.grid(row=2, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(columnspan=3 ,row=2, column=1)

L2 = Label (my_app, text = 'lebar : ')
L2.grid(row=3, column=0)
str2 = StringVar()
E2 = Entry(my_app, textvariable=str2)
E2.grid(columnspan=3 ,row=3, column=1)

L3 = Label (my_app, text = 'Tinggi : ')
L3.grid(row=4, column=0)
str3 = StringVar()
E3 = Entry(my_app, textvariable=str3)
E3.grid(columnspan=3 ,row=4, column=1)

def luas():
    p=float(str1.get())
    l=float(str2.get())
    t=float(str3.get())
    w=2*((p*l)+(p*t)+(l*t))
    LP.config(text=w)

B = Button(my_app, text='Hitung Luas', command= luas)
B.grid(row=5,column=0)
L=Label(my_app, text='luas :',font='Helvetica 10 bold')
L.grid(row=5,column=2)
LP=Label(my_app, text='0')
LP.grid(row=5,column=3)

my_app.mainloop()








