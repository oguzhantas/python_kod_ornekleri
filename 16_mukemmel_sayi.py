#mükemmel sayı, tüm bölenleri toplamı kendine eşit
# olan sayıdır, örneğin 6=1+2+3, 28=1+2+4+7+14
sayi = int(input('Sayı giriniz:'))
toplam=0
for i in range(1,sayi):
    if (sayi%i==0):
        print(sayi, " sayısını ",i," tam böler")
        toplam+=i
if (toplam==sayi):
    print(sayi, " sayısı mükemmel sayıdır.")
else:
    print(sayi, " mükemmel değil")
