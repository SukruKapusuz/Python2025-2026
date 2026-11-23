Sinav_not=int(input("notunuzu giriniz : "))

if Sinav_not>=50  and    70>Sinav_not :
    print("notu C")
elif Sinav_not>=70 and    85>Sinav_not  :
    print("notu B")
elif Sinav_not>=85  and  100>=Sinav_not:
    print("notu A")
elif Sinav_not<0 or Sinav_not>100:
    print("Girdiğiniz not hatalı")
else:
    print("Kaldı")