#1den 10 a sayıların ortalaması

kac=int(input("kaça kadar ki sayıların toplamı-->"))
toplam=0
for i in range(kac):
    toplam+=i
    i+=1

ort=toplam/kac

print(ort)