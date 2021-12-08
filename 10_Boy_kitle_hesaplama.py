boy=float(input("Boyunuzu giriniz:"))
kilo=float(input("Kilonuzu giriniz:"))
BKI= kilo/boy**2
print("Boy kitle indeksiniz",BKI)

if (BKI<20):
    print("Zayıf")
elif(BKI>=20 and BKI<25):
    print("Normal")
elif(BKI>=25 and BKI<30):
    print("Hafif Şişman")
elif(BKI>=30 and BKI<35):
    print("Şişman")
elif(BKI>=35 and BKI<45):
    print("Sağlık açısından önemli")
elif(BKI>=45 and BKI<50):
    print("Aşırı Şişman")
elif (BKI>=50):
    print("Morbid")

