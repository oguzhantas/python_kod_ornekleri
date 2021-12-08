
markalar=["BMW","Mercedes","Volvo","Audi","Volvo","VW","Volvo"]

print(markalar.index("Volvo")) #aradığın elemanın indeksini döndürür
#Listede 2 tane Volvo var ama ilk karşılaştığını döndürür.

print(markalar.count("Volvo")) #yazılan elemandan kaç tane olduğunu sayar

markalar.sort() #sıralama yapar
print(markalar)

markalar.reverse() #ters çevirir
print(markalar)

markalar2 = markalar.copy()
print(markalar2)
del markalar[4]
print(markalar)