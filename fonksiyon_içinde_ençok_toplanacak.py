def topla():
    toplam=0
    sayı=int(input("kaça kadar toplayacan..."))
    for i in range(1,sayı+1):
        toplam=toplam+i
    return toplam


print(topla())