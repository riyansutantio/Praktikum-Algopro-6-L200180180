import socket
import platform
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50015))
s.listen(5)
print 'Server penjawab otomatis sudah siap!!'
data = ''
machine=platform.machine()
release=platform.release()
system=platform.system()
version=platform.version()
node=platform.node()
kamus = {'machine'  : machine,
         'release'  : release,
         'system'   : system,
         'version'  : version,
         'node'     : node, 
        }
while data.lower() !='q' :
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower()=='q':
            print('SIAP !!')
            s.close()
            break
        print 'Permintaan:' , data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf perintah tidak di mengerti')
