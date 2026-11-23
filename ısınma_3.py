#basamak değerleri toplamı 10 dan büyük ise vav yazan değil ise miyav yazsın


okul_Num1=int(input("okul numaranızın ilk rakamını  giriniz-->"))
okul_Num2=int(input("okul numaranızın 2. rakamını giriniz-->"))
okul_Num3=int(input("okul numaranızın 3. rakamını giriniz-->"))


toplam=okul_Num1+okul_Num2+okul_Num3


if toplam>10:
    print("woow")
else:
    print("miyav")