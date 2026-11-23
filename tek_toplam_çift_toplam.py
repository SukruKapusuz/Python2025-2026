#1den 10 a kadar toplama tek çift
print("---1 den 10 a topla---")
print("hem tek topla hem çift")




toplamcift=0
for i in range(1,11):
    if i%2==0:
       toplamcift+=i
       i+=1
print("çift toplam-->",toplamcift)



toplamtek=0
for i in range(1,11):
    if i%2==1:
       toplamtek+=i
       i+=1
print("tek toplam-->",toplamtek)






toplam=toplamtek+toplamcift
print("tamamının toplamı",toplam)