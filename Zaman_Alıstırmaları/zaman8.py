import datetime

bugun = datetime.datetime.today()
fark = datetime.timedelta(days=150)
gelecek=bugun+fark

print("150 gün sonrası :", gelecek)

print("Biçimlendirilmiş Tarih :", gelecek.strftime('%c'))