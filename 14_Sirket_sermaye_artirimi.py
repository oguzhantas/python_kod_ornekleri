# Bir şirketin başlangıç sermayes 10.000 TL olsun
# Şirket her yıl %10 büyürse 20 yıl sonra sermayesi ne kadar olur?


sermaye = int(input("Şirket başlangıç sermayesini giriniz:"))
#örneğin 1000
# 1. yıl %10 büyürse 1000'in %10'u 100 TL, sermaye=1100 TL
# 2. yıl %10 büyürse 1100'ün %10'u 110 TL  sermaye=1210 TL
# ...
for x in range(1,21):
    print(x,". Yıl Sermaye :",round(sermaye,2))
    sermaye = sermaye + sermaye*10/100;
    #sermaye += sermaye *10/100


