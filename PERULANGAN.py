'''
Edwin Mahendra/ 71200541

Soal:
buatlah program untuk menghitung banyaknya huruf vokal dan konsonan
dari setiap kalimat atau kata yang diinputkan.
gunakan fungsi ord()!

ket:
A=65
E=69
I=73
O=79
U=85

a=97
e=101
i=105
o=111
u=117

'''
a=input('masukkan kata=')
voc=0
con=0
for i in a:
    if(ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85 or ord(i)==97 or ord(i)==101 or ord(i)==105 or ord(i)==111 or ord(i)==117):
        voc=voc+1
    elif((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
        con=con+1
print('jadi total huruf vokal= ',voc)
print('jadi total huruf konsonan= ',con)