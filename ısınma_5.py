#kişi girdiği toplam negatif çıkıyor ise "hop dur orda diyecek"

sayı1=int(input("toplanacak 1. sayıyı giriniz-->"))
sayı2=int(input("sayı 2 yi giriniz-->"))

toplam=sayı1+sayı2


if toplam>0:
    if toplam>10:
        print("vav")
    elif toplam<5:
        print("miyav")
    elif toplam>5 and toplam<10:
        print("hav")
    else:
        print("?")
elif toplam<0:
    print("hop dur orada")