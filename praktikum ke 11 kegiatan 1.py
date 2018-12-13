from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Data Diri')

L = Label(my_app, text ='Data Diri', font=('Arial', 24))
L.grid(row=0, column=0)

L1 = Label (my_app, text = 'Nama : ')
L1.grid(row=1, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(row=1, column=1)
          
L2 = Label (my_app, text = 'NIM : ')
L2.grid(row=2, column=0)
str2 = StringVar()
E2 = Entry(my_app, textvariable=str2)
E2.grid(row=2, column=1)

L3 = Label (my_app, text = 'Idola Dikalangan sahabat : ')
L3.grid(row=3, column=0)
str3 = StringVar()
E3 = Entry(my_app, textvariable=str3)
E3.grid(row=3, column=1)

L4 = Label (my_app, text = 'MOtto : ')
L4.grid(row=4, column=0)
str4 = StringVar()
E4 = Entry(my_app, textvariable=str4)
E4.grid(row=4, column=1)

L5 = Label (my_app, text = 'Buku favorit : ')
L5.grid(row=1, column=0)
str5 = StringVar()
E5 = Entry(my_app, textvariable=str5)
E5.grid(row=1, column=1)

def info():
        my_app.destroy()

B1 = Button(my_app, text='Tutup', command= info)
B1.grid(row=6, column=1)

my_app.mainloop()
