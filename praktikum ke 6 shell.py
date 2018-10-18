Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> Username
'Bangkit1199'
>>> Password
'riy32'
>>> Nama = 'Riyan Sutantio Bangkit Nugroho'
>>> NIM = 'L200180180'
>>> X = '1' + NIM[7:] # Didalam string, digabungkan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh dari variabel NIM sampai selesai
>>> print(X)
1180
>>> a = int(X) # Konversi string ke integer (bilangan bulat)
>>> print(a)
1180
>>> b = len(Nama) #konversi string dalam variabel Nama ke dalam angka
>>> print(b)
30
>>> type(a) #Menampilkan type data dari variabel a
<type 'int'>
>>> type(b) #Menampilkan type data dari variabel b
<type 'int'>
>>> a/b # Operasi pembagaian antara bilangan variabel a dangan b. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/floating point semua dan apabila salah satu data bertype integer sedangkan yang lain dengan type floating point. Data dengan type string tidak bisa diolah menggunakan operasi ini
39
>>> a//b # Operasi pembagian antara bilangan dengan pembulatan ke bawah. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/floating point semua dan apabila salah satu data bertype integer sedangkan yang lain dengan type floating point. Data dengan type string tidak bisa diolah menggunakan operasi ini
39
>>> 10*(a-999) # Operasi perkalian ini dapat digunakan untuk mengalikan data dengan type integer dengan integer, floating point dengan floating point, integer dengan floating point, dan dapat juga untuk menggabungkan berulang pada string dengan menggunakan type data integer. Namun, penggabungan berulang kata ini tidak berlaku untuk data dengan type floating point dengan string
1810
>>> b**2 # operasi ini digunakan untuk perpangkatan
900
>>> a%b # Operasi ini digunakan untuk memunculkan sisa hasil bagi
10
>>> c = 12.5 # Memasukkan nilai 12.5 ke dalam variabel c
>>> type(c) # Menampilkan tipe data dari variabel c
<type 'float'>
>>> a/c # Operasi pembagian variabel a dengan variabel c
94.4
>>> a//c # Operasi pembagian antara variabel a dengan variabel c dengan pembulatan ke bawah
94.0
>>> a%c # Operasi ini digunakan untuk memunculkan sisa hasil bagi
5.0
>>> c>b # Operasi ini digunakan untuk menampilkan perbandingan lebih besar dari
False
>>> type(c>b) # Menampilkan type data dari (c>b)
<type 'bool'>
>>> a>b and b>c # Pada data terdapat dua pernyataan, kedua pernyataan tersebut dihubungkan dengan operator logika "and" maka bila kedua pernyataan tersebut bernilai benar maka hasilyang muncul pada operasi adalah "False" dan bila kedua pernyataan nya salah maka hasil operasi yang muncul adalah "False"
True
>>> a>1100 or b<10 # logika yang digunakan pada data adalah "or". Dari pernyataan disamping diartikan 1180 > 1100 atau 30 < 10. Dengan 1180 > 1100 adalah data pertama dan 30 < 10 sebagai data kedua.  Hasil dari operasi disamping bernilai "True" karena menggunakan logika "atau". Apabila kedua data bernilai benar maka "True", salah satu dari data bernilai benar maka "True" namun apabila kedua data bernilai salah maka "False" yang akan muncul pada hasil operasi
True
>>> 
