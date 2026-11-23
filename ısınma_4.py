#5 den küçük miyav 10 dan küçük hav 10 büyük vav


okul_Num1=int(input("okul numaranızın ilk rakamını  giriniz-->"))
okul_Num2=int(input("okul numaranızın 2. rakamını giriniz-->"))
okul_Num3=int(input("okul numaranızın 3. rakamını giriniz-->"))


toplam=okul_Num1+okul_Num2+okul_Num3


if toplam>10:
    print("woow")
elif toplam<5:
    print("miyav")
elif toplam>5 and toplam<10:
    print("hav")
else:
    print("?")

    