print("-------------------------------------------------------------------")
print("Tarifenize Tanımlı Konuşma Süresi      :  1000 Dk.")
print("Tarifenize Tanımlı Mesaj Adeti         :  1000 SMS")
print("Tarifenize Tanımlı İnternet Paketi     :  5000 MB  (5 GB)")
print("  ")
print( "  ")
print("İnternetiniz Bittiğinde Kullanım Ücretlendirmesi        Her 100 MB için 5 TL'dir")
print("Dakikalarınız Bittiğinde Kullanım Ücretlendirmesi       50 Kr/Dk")
print("SMS'leriniz Bittiğinde Kullanım Ücretlendirmesi         50 Kr/SMS")
print("___________________________________________________________________")
print("AYLIK TARİFE TUTARINIZ                 :  30 TL          ")
print( "  ")
print("  ")
print("  Lütfen kullanım miktarlarınızı girerek faturanızı sorgulayınız...")
konuş=int(input("Aylık kullandığınız konuşma dakikanızı giriniz  : "))
sms=int  (input("Aylık kullandığınız SMS adetini giriniz         : "))
net=int(input  ("Aylık kullandığınız internet miktarını giriniz  : "))
print("  ")
print("...................................................................")

asım_konuş=float(konuş-1000)*0,5
asım_sms=float(sms-1000)*0,5
asım_net=int((net-5000)/100)*5
fatra=0
fatra=fatra + asım_konuş
fatra=fatra + asım_net
fatra=fatra + asım_sms

if asım_net>0 or asım_sms>0 or asım_konuş>0:
    print("TARİFENİZDE PAKET AŞIMI BULUNMAKTADIR :(")
    print("TOPLAM FATURA TUTARINIZ  :  ",fatura+30)
else:
    print("TARİFENİZDE HEER HANGİ BİR AŞIM YOKTUR   :)")
    print("TOPLAM FATURA TUTARINIZ :  ",30)

