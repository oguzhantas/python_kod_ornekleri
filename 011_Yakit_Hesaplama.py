# Kaç TL'lik benzin alınacak
# Benzinin litresi ne kadar, klavyeden alınacak
# Kaç litre benzin alınmıştır, hesaplayınız.
ucret=float(input("Kaç TL ile benzin alınacak:")) #200 TL
litreFiyat=float(input("benzinin Litresi kaç TL:")) #7.18 TL

miktar = ucret/litreFiyat #kaç litre alabileceğini hesapladık
print("Yaptığınız ödemeyle",miktar," litre kadar benzin alabilirsiniz")

depomiktar= int(input("Arabanızın deposu maksimum kaç litre benzin alıyor:"))
kalan=depomiktar-miktar;

print("Deponuzun tamamen dolması için ",kalan," litre kadar benzin almalısınız");
kalanOdenecek=kalan*litreFiyat;
print("Deponuzun tamamen dolması için ",kalanOdenecek," kadar ödemelisiniz" );


