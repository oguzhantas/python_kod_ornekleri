# continue komutu while döngüsü içinde belli bir durumla
# karşılaşınca döngünün başına gider
# Aşağıdaki döngü 1'den 100'e kadar sayıları yazdıracak
# fakat 10 değerine gelince atlayacak
x=0
while(x<10):
    x += 1
    if (x == 5):
        continue
    print(x)




