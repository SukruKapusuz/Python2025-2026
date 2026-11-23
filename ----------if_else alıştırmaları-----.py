 
#---------
#sayfa 73
#---------

#a
 
print("sınıfı geçtiniz mi? kaldınız mı? öğrenmek içün notlarınızı giriniz")

not1=int (input  ("Lütfen 1. notunuzu giriniz  :  "))
not2=int (input  ("Lütfen 2. notunuzu giriniz  :  "))
not3=int (input  ("Lütfen 3. notunuzu giriniz  :  "))

orta=(not1+not2+not3)/3

if orta<50:
    print("kaldınız")
else:
    print("geçtiniz")





#b

print("açılarını bildiğiniz şeklin üçgen olup olmmadığını öğrenmek için açıları giriniz")

acı1=int(input("1.açıyı giriniz :  "))
acı2=int(input("2.açıyı giriniz :  "))
acı3=int(input("3.açıyı giriniz :  "))

toplam= acı1+acı2+acı3

if toplam==180:
    print("Bu açılar bir üçgene ait")
else:
    print( "Bu açılar bir üçgene ait değil")


#c

print("havayolu ulaşımında bagaj hakkı sorgulamak için valiz ağırlığını giriniz")

agırlık=int(input("valiz ağrılığınızı giriniz  :  "))

fazlalik=agırlık-20
fazla_deger=fazlalik*10


if agırlık<=20:
    print("fazla ücrete gerek yok")
else:
    print("bilet ücret üstüne")
    print(fazla_deger)
    print("tl ödemeniz gerekir")




#ç

print("satın alım için gereken meblağ indirim için uygun mu")
meblag=int(input("satın alım için gereken meblağ  :"))
 
if meblag<200:
    print("sana indirim yok")
else:
    print("%25 indirim var")


#------------
#sayfa 80 
#------------

#sıra sizde

#a

ad=str(input("Kullanıcı adını giriniz : "))
sifre=str(input("şifrenizi giriniz"))

if sifre==1923: 
    if ad=="Türkiye":
        print("giriş başarılı")
    else:
        print("Yanlış girdiniz")
else:
     print("Yanlış girdiniz")

#sıra sizde


işlemci=str(input("İşlemci türünü giriniz (intel) : "))
ram=int(input("RAM değerinizi giriniz (gb)  : "))

if işlemci=="i7" or 8<=ram:
    print("çalışır")
else: 
    print("çalışmaz")

#------------
#sayfa 81
#------------

#sıra sizde

plaka=str(input("Memleketiniz plaka kodunu giriniz : "))

if plaka=="06":
    print("ANKARA")
elif plaka=="07":
    print("ANTALYA")
elif plaka=="08":
    print("ARTVİN")
elif plaka=="38":
    print("KAYSERİİ!")
else:
    print("Türkiye")


#------------
#sayfa 82
#------------

#a

hava=int(input("Hava durumunu sayı şeklinde giriniz :"))

if hava<=5:
    print("soğuk")
elif hava<=14 and hava>=6:
    print("ılık")
else:
    print("sıcak")

#b

print("otoparkta aracınızın bulunduğu toplam vakti giriniz")

vakit=int(input("saat cinsinden giriniz  :  "))

if vakit==0:
    print("5 TL")

elif vakit>=5:
    print("toplam ücret")
    print(vakit*5)
    print("tl dir")
else:
    print("toplam ücret")
    print(vakit*3)
    print("tl dir")


#ç

boy=int(input("boyunuzu metre cinsinden giriniz : "))
agırlık2=int(input("ağırlığınızı giriniz : "))

vki=agırlık2/(boy*boy)


if vki<25 and vki>=18:
    print("normal")
elif vki<=25 and vki>30:
    print("kilolusunuz")
elif vki<=30 and vki>35:
    print("obez")
else:
    print("ciddi obez")


#d

ad2=str(input("Adınızı giriniz :  "))
maaş=int(input("Maaşınızı giriniz :  "))
yıl=int(input("çalışma yılınızı giriniz :  "))

if yıl>=5:
    print("Sayın")
    print(ad2)
    print("zamlı maaşınız:")
    print(maaş+(maaş%10))
    print("TL")
     
elif yıl<6 and yıl>=10:
    print("Sayın")
    print(ad2)
    print("zamlı maaşınız:")
    print(maaş+(maaş%15))
    print("TL")

elif yıl<10:
    print("Sayın")
    print(ad2)
    print("zamlı maaşınız:")
    print(maaş+(maaş%25))
    print("TL")


#e
sayı1=int(input("sayı 1 i giriniz :  "))
sayı2=int(input("sayı 2 yi giriniz :  "))
sayı3=int(input("sayı 3 ü giriniz :  "))

if sayı1>sayı2 and sayı1>sayı3:
    print(sayı1,"en büyükleri ")
elif sayı2>sayı1 and sayı2>sayı3:
    print(sayı2,"en büyükleri")
else:
    print(sayı3," en büyükleri")

#------------
#sayfa 83
#------------

#sıra sizde

öğrenci=str(input("öğrenci misiniz? (e) (h)   : "))
ne_izler=str(input("Sinema mı? Tiyatro mu? (s) (t) : "))


if ne_izler=="t":
    if öğrenci=="e":
        print("ücret 5 TL")
    else:
        print("10 TL")
else:
    if öğrenci=="e":
        print("ücret 7,5 TL ")
    else:
        print("ücreti 15 tl")