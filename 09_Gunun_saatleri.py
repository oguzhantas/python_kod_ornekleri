
saat=int(input("Günün saatini giriniz(0-23)"))

if (saat>=6 and saat<12):
    print("Günaydın")
elif(saat>=12 and saat<17):
    print("Tünaydın")
elif(saat>=17 and saat<20):
    print("İyi akşamlar")

elif(saat>=20 and saat<24):
    print("İyi geceler")
elif(saat>0 and saat<6):
    print("İyi uykular")