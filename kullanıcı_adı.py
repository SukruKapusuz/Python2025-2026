#kullanıcı adı veli şifre 1234 
while True:

    kullanıcı_adı=str(input("Kullanıcı adını giriiz-->"))


    sifre=int(input("Şifre giriniz-->"))


    if kullanıcı_adı=="veli":
        if sifre==1234:
            print("giriş başarılı")
        else:
            print("başarısız deneme")
    else:
        print("başaarısız deneme")





