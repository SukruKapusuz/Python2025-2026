sayı=int(input("faktöriyel içinde değerini öğrenmek istediğiniz sayıyı giriniz==>"))
faktöriyel=sayı

for sayi in range (1,sayı):
    faktöriyel=sayi*faktöriyel

print (faktöriyel)