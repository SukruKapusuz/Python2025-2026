#kullanıcı adı veli şifre 1234 
import random
hak=3
while True:

    robot=random.randint(1000,9999)
    print(robot)
    print("lütfen rakamları tekrarlayınız")
    giris=int(input("--->"))
    if robot==giris:
        print("giriş başarılı")

    else:
        print("robotsun sen?")
        break


    kullanıcı_adı=str(input("Kullanıcı adını giriniz-->"))
    sifre=int(input(        "Şifre giriniz------------>"))
    
    
    
    if hak<0:
        print("hakkın bitti :(")
        break

    if kullanıcı_adı=="veli":
        if sifre==1234:
            print("------------------")
            print("giriş başarılı")
            print("------------------")
            continue
        else:
            print("başarısız deneme")
            hak=hak-1
    else:
        print("başarısız deneme")
        hak=hak-1

   