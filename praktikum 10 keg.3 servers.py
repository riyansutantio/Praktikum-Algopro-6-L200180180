import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50505))
s.listen(5)
print "Server sudah sangat siap siap"
perintah = ''
p=0
l=0
t=0
x=''
while comm != 'keluar':
    komm, addr = s.accept()
    while comm != 'keluar':
        base = komm.recv(1024).lower().split("=")
        comm = base[0]
        if comm == 'keluar':
            s.close()
            break
        print 'Input:', comm
        if len(base) == 2 :
            if comm == 'panjang':
                p = int(base[1])
                balasan = "Nilai panjang tercatat"
                komm.send(balasan)
            elif comm == 'lebar':
                l = int(base[1])
                balasan = "Nilai lebar tercatat"
                komm.send(balasan)
            elif comm == 'tinggi':
                t = int(base[1])
                balasan = "nilai tinggi tercatat"
                komm.send(balasan)
            
        elif comm == 'hitung':
            L = int((p*l+p*t+l*t)*2)
            balasan = "Luas balok dengan panjang: {}, lebar: {}, dan tinggi: {} adalah {}".format(p,l,t,L)
            komm.send(balasan)
        else:
            komm.send('pesan tidak dikenal')
