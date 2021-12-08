#sonsuz kere soru soracak, sadece Q veya q girince döngüden çıkacak

while True:
    g = input('Hangi ışık(K,S,Y):')
    if(g=='K' or g=='k'):
        print('Dur')
    elif(g=='S' or g=='s'):
        print('Bekle')
    elif(g=='Y' or g=='y'):
        print('Geç')
    elif(g=='Q' or g=='q'):
        break
    else:
        print('K,Y,S veya çıkmak için Q giriniz.')
