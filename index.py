def hitunglah(panjang,lebar,tinggi) :
    p=panjang
    l=lebar
    t=tinggi
    luas=2*((p*l)+(p*t)+(t*l))
    return luas
panjang = 5
lebar = 6
tinggi = 7

print "<!DOCTYPE html>"
print
print """<html>
<head><title>Luas Bangun Geometri</title></head>
<body>"""
print """<table>
<tr>
    <th rowspan='8' width='150'> GAMBAR </th>
    <td><h3> Bangun Geometri <h3></td>
</tr>
<tr>
    <td>Nama Bangun</td>
    <td>:</td>
    <td>Balok</td>
</tr>
<tr>
    <td>Dimensi (2D/3D)</td>
    <td>:</td>
    <td>3d</td>
</tr>
<tr>
    <td>Rumus Luas</td>
    <td>:</td>
    <td>2*((p*l)+(p*t)+(t*l))</td>
</tr>
<tr>
    <td>Panjang</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(panjang)
print """<tr>
    <td>Tinggi</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(tinggi)
print """<tr>
    <td>lebar</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(lebar)
print """<tr>
    <td>Luas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(hitunglah(panjang,lebar,tinggi))
print"""
</table>"""

print"</body></html>"
