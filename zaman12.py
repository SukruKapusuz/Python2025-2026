import datetime
import locale 

locale.setlocale(locale.LC_ALL, 'Turkish.1254')

tarih_metni = '29 Ekim 1923 Saat 14:32:11'
print("metin halindeki tarih = ", tarih_metni)
tarih_nesnesi = datetime.datetime.strptime(tarih_metni,'%d %B %Y saat %H:%M:%S')
print("tarih nesnesi = ",tarih_nesnesi) 
print(tarih_nesnesi)
print(tarih_nesnesi.month)
print(tarih_nesnesi.day)
