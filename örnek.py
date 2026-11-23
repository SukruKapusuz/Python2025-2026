#Öğrenci Not Hesaplama Sistemi
#Soru: Kullanıcıdan bir öğrencinin vize ve final notunu alan, vizenin %40'ını ve finalin %60'ını 
#hesaplayarak ortalamayı bulan ve harf notunu (AA, BA, FF vb.) ekrana yazdıran Python kodunu yazınız.
#Koşul: Final notu 50'nin altındaysa, ortalama kaç olursa olsun öğrenci "FF" ile kalsın.
#Harf Notu: 90-100: AA, 70-89: BA, 50-69: CC, 0-49: FF.



vize=int(input(  "vize notunuzu giriniz--->"))
final=int(input( "final notunuzu giriniz-->"))

vize_ort=(vize*40)/100
final_ort=(final/60)/100
 
toplam=vize_ort+final_ort

if 100>=toplam>=90:
    print("AA")
elif 90>toplam>=70:
    print("BA")
elif 70>toplam>=50:
    print("CC")
elif 50>toplam>=0:
    print("FF")
else:
    print("Ne diyon dayı!")