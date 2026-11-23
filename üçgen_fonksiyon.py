print("açılarını bildiğiniz şeklin üçgen olup olmmadığını öğrenmek için açıları giriniz")

acı1=int(input("1.açıyı giriniz :  "))
acı2=int(input("2.açıyı giriniz :  "))
acı3=int(input("3.açıyı giriniz :  "))
def ucgenmi(a,b,c):

    toplam= a+b+c

    if toplam==180:
        return True
    else:
        return False
    

if ucgenmi(acı1,acı2,acı3)==True:
    print("Bu açılar bir üçgene ait")
else:
    print( "Bu açılar bir üçgene ait değil")