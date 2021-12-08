print('1) Latte       10 TL')
print('2) Americano   8 TL')
print('3) Macchiato    12 TL')
print('4) Filtre      9 TL')
secim=int(input('Seçiminiz yapınız:'))
adet =int(input('Kaç adet:'))

if (secim==1):
    toplam=adet*10
elif(secim==2):
    toplam=adet*8
elif(secim==3):
    toplam=adet*12
elif(secim==4):
    toplam=adet*9
else:
    print('Lütfen 1-4 arası seçim yapınız')

print('Toplam ödenecek:',toplam)



