a= int(input("1. sayıyı giriniz:"))
b= int(input("2. sayıyı giriniz:"))
islem=input("Toplama(+), Çıkarma(-), Çarpma(*), Bölme(/)");
sonuc=0

if (islem=="+"):
    sonuc=a+b #toplama

elif(islem=="-"):
    sonuc=a-b #Çıkarma

elif(islem=="/"):
    sonuc=a/b #bölme

elif(islem=="*"):
    sonuc=a*b #çarpma

else:
    print("Lütfen +,-,*,/ işaretlerinden birini giriniz")

print("İşlem Sonucu:",sonuc);

