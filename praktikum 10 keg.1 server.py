import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 5004))
s.listen(5)
print 'Server penjawab otomatis sudah siap'
data = ''
kamus = {'nama'     : 'Riyan Sutantio Bangkit Nugroho',
         'NIM'      : 'L200180180',
         'angkatan' : 'Angkatan 18',
         }
while data.lower() !='q' :
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower()=='q':
            print('SIAP !!!')
            s.close()
            break
        print 'permintaan:' , data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('maaf perintah tidak di mengerti')
