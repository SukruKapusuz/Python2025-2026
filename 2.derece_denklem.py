kare=int(input("karesi alınacak olanı giriniz :  "))
kat=int(input("katsayısı olanı giriniz :  "))
sabit=int(input("sabit olanı giriniz :  "))
tum=0
tek=0
def delta(a,b,c):
    delta=(b**2)-(4*a*c)

    if delta>0:
        x1=(-b+delta**(1/2))/2*a
        x2=(-b-delta**(0.5))/2*a
        tum=[x1,x2]
        return tum
    elif delta==0:
        x1=x2=(-b)/2(a*a)
        return x1
    elif delta<0:
        return 0

if delta(kare,kat,sabit)==tum:
    print(tum)
elif delta(kare,kat,sabit)==tek:
    print("delta" ,tek)
elif delta(kare,kat,sabit)==0:
    print("reel kök yoktur")