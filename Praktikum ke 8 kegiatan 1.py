V = {'NIM':'L200180180','Nama':'Riyan Sutantio B.N.','Alamat':'Sukoharjo','Kode Pos':'57514', 'Umur':'19','Jurusan':'Informatika','Fakultas':'FKI'}

print "Pilihan yang tersedia:"
print "N menampilkan Nama"
print "n menampilkan NIM"
print "l menampilkan Alamat"
print "p menampilkan Kode Pos"
print "r menampilkan Umur"
print "f menampilkan Jurusan"
print "u menampilkan Fakulas"


def Nama():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Nama:' + V['Nama']

def NIM():
        "menampilkan data diri masing masing 1 setiap data"
        print 'NIM:' + V['NIM']

def Alamat():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Alamat:' + V['Alamat']

def Kodepos():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Kode Pos:' + V['Kode Pos']

def Umur():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Umur:' + V['Umur']

def Jurusan():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Jurusan:' + V['Jurusan']

def Fakultas():
        "menampilkan data diri masing masing 1 setiap data"
        print 'Fakulas:' + V['Fakultas']

repeat = True

while repeat :
    x = raw_input("Pilihan Saudara:")
    if x == "N" :
        Nama()
    elif x == "n" :
        NIM ()
    elif x == "l" :
        Alamat ()
    elif x == "p" :
        Kodepos ()
    elif x == "r" :
        Umur ()
    elif x == "f" :
        Jurusan ()
    elif x == "u" :
        Fakultas ()
    elif x == "k" :
        print "Terimakasih."
        break
repeat = False
