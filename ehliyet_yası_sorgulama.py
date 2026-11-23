
print("Ehliyet yaşı sorgulamak için...")
yas=int(input("Yaşınızı giriniz : "))
if yas>=22:
    print("Ağır vasıta dahil her türlü ehliyeti alabilirsin.")
elif yas>=18 and 22>yas:
    print("ehliyet alabilirsiniz.")
elif yas>=16 and yas<18:
    print("Motor ehliyeti için yaşınız uygundur.")
else:
    print("Yaşınız ehliyet almaya uygun değil.")