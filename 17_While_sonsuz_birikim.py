#Bir kişinin başlangıçta 300 TL'si olduğunu
#düşünelim her ay bunun üzerine %10 fazla biriktirdiğinde
# kaç ay sonra 100.000 TL'si olur.

s=1000 #sınır para miktarı
toplam=300 #başlangıçtaki para miktarı
n=0
while(True):
    n+=1
    toplam += toplam * 10 / 100
    print(n, ".ay biriken para:", toplam)
    if(toplam>=s):
        break
#print("Ay sayısı:",n)
#print("Biriken para:",t)

