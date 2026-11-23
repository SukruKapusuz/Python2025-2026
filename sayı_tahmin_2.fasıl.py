while (True):
    import random
    sayı=random.randint(1, 10)

    asgari=5
    
    while (True):
        tahmin=int(input("1 ile 10 arasında bir sayı tahmin ediniz  : "))
        if asgari<=0:
            print("kaybettiniz")
            break
        
        
        if tahmin==sayı:
            print("tebrikler bildiniz.")
            break
        elif tahmin>10 or tahmin<0:
            print("yanlış değer girdiniz")
        elif tahmin>sayı:
            print("büyük sayı girdiniz tekrar seçin.")
            asgari=asgari-1
            print("kalan deneme hakkı--> ",asgari)
        elif tahmin<sayı:
            print(" küçük oldu tekrar seç.")
            asgari=asgari-1
            print("kalan deneme hakkı--> ",asgari)
        else:
            print("lütfen sayı giriniz.....") 







    


    print("Başka sayı tahmin edelim mi?")
    evet=str(input("(e)(h)"))
    if evet=="e":
        continue
    elif evet=="h":
        break
    else:
        print("bu yanlış tuşu HAYIR anlıyorum-->")
        break
    