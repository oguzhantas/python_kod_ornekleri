#tuple içindeki elemanlar değiştirilemez
alisveris=("elma","çikolata","cips","meyve suyu","elma")
print(alisveris)
#alisveris[2]="kivi" #hata verir
liste_alisveris=list(alisveris) #tupples listeye çevrilerek değişim sağlanıyor
liste_alisveris[2]="kivi"
print(liste_alisveris)

sonuc= "elma" in alisveris
print(sonuc)

sonuc= "armut" in alisveris
print(sonuc)

print(alisveris)
print("Uzunluk:",len(alisveris))

print("Elmadan kaç tane var:",alisveris.count("elma"))
#bir elemandan kaç adet var, onu sayar

print(alisveris[1:4]) #çikolata, cips, meyve suyu yazdırır
print(alisveris[:]) # tüm elemanları yazdır
print(alisveris[:4]) # baştan 4.elemana kadar yazdır
print(alisveris[-2]) #en son elemandan bir öncekini yazdırır

del alisveris
#print(alisveris) #hata verir, çünkü sildik
tekrarli_tuple = ("python",)*3 #tekrarlıyoruz
print(tekrarli_tuple) # 3 defa python yazar
