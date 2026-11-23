#kullanıcı adı veli şifre 1234 
hak=3
while True:

    kullanıcı_adı=str(input("Kullanıcı adını giriniz-->"))


    sifre=int(input("Şifre giriniz-->"))
    
    
    
    if hak<0:
        print("hakkın bitti")
        break

    if kullanıcı_adı=="veli":
        if sifre==1234:
            print("giriş başarılı")
            continue
        else:
            print("başarısız deneme")
            hak=hak-1
    else:
        print("başaarısız deneme")
        hak=hak-1

   