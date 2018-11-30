##kegiatan 1
berkas = open("L200180180","w")
berkas.write("L200180180 \n")
berkas.write("23-11-1999 \n") 
berkas.write("riyan sutantio  \n") 
berkas.close() 

## Kegiatan 2 
berkas = open('L200180180','r') 
NIM = berkas.readline() 
Tanggal = berkas.readline() 
Nama = berkas.readline() 
ttlmm = "23/11/99 \n" 
kota = "sukoharjo " 
berkas.close() 

berkas = open('L200180180','w') 
berkas.write (Nama) 
berkas.write (kota) 
berkas.write (ttlmm) 
berkas.write (NIM) 
berkas.close() 

## Kegiatan 3 dan 4. 

import shelve 
C = open("L200180180","r") 
D = shelve.open("riyan.data") 
D["berkas"] = C.read() 
D.close() 
C.close() 

D = shelve.open("riyan.data") 
print(D["berkas"]) 
D.close() 
