import socket
hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50505))
print "Menghitung luas Balok"
while pesan.lower() != 'keluar':
    if pesan.lower() != 'keluar':
        pesan = raw_input('Input: ')
        s.send(pesan)
        
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'Respon:', response
    else:
        print "Respon: -"
s.close()
