from datetime import datetime

bugun = datetime.today()

print("Bu günün tarihi", bugun)

yıl = int(input("Lütfen doğduğunuz yılı girin--->"))
ay  = int(input("Lütfen doğduğunuz ayı girin---->"))
gün = int(input("Lütfen doğduğunuz günü girin--->"))
dogum = datetime(year=yıl,month=ay,day=gün)

yas = bugun-dogum
print(yas)