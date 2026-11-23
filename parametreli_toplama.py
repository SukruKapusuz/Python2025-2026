def topla(sayi):
    bitis=int(input("Kaça Kadar olan Sayıları Toplayacaksın"))
    toplam=0    
    for i in range(sayi,bitis+1):
        toplam=toplam+i
    print("Fonksiyon da-->",toplam)
    return toplam

kac=int(input("kaç' başlasın toplayacağın değerler---->"))
donenToplam = topla(kac)
print("Ana Kodda Yazdır-->" , donenToplam)