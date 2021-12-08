sayi = int(input('İkilik tabana çevrielecek sayıyı giriniz:'))
sonuc=""
while(True):
        kalan=sayi%2
        sonuc+=str(kalan)
        sayi=sayi//2
        print("Sayı:",sayi,"Kalan:",kalan)
        if (sayi<2):
            sonuc+=str(kalan)
            break
        else:
            continue
a=""
#şimdi ters çeviriyoruz
for i in range(0,len(sonuc)):
    a+=sonuc[len(sonuc)-i-1]

print(a)





