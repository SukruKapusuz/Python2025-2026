tekToplam=0
ciftToplam=0
tekAdet=0
ciftAdet=0
sayı=int(input("bitiş sayıyı==>"))
for  sayılar in range (sayı):
        if sayı%2==0:
            cifttoplam=cifttoplam+sayı
            ciftAdet=ciftAdet+1
        else:
            tektoplam=tektoplam+sayı
            tekAdetAdet=tekAdet+1
    

print("tek sayıların toplamı :",tektoplam/tekAdet)

print("çift sayıların toplamı :",cifttoplam/ciftAdet)