#iki sayı arasındaki toplam bulma
s1= int(input("1. sayıyı giriniz:"))  #5 olsun
s2= int(input("2. sayıyı giriniz:"))  #10 olsun

toplam=0
i=s1
while (i<=s2):
    print(i)
    toplam=toplam+i
    i=i+1

print("Toplam sonucu:", toplam)