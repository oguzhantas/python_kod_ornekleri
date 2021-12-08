# 0!=1
# 1!=1
# 2!= 1.2
# 3! = 1.2.3
sayi = int(input("Faktöriyeli alınacak sayı:"))
if (sayi==0):
    print("Faktöriyel işlemi sonucu:1")
elif (sayi>0):
    i = 1
    fakt = 1
    while (i <= sayi):
        fakt *= i
        i += 1
    print("Faktöriyel işlemi sonucu:", fakt)
