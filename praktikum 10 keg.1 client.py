import socket

hostname = 'localhost'
pesan =''
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,5004))
print 'Mesin penjawab otomatis sudah siap!!'
while pesan.lower() !='q' :
    pesan = raw_input('Pertanyaan : ')
    s.send(pesan)
    if pesan.lower()=='keluar':
            print('SIAP !!')
            s.close()
            break
    elif pesan.lower() !='q':
        response =s.recv(1024)
        print 'Jawab :' , response
s.close()
