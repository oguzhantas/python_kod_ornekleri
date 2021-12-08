puan=0
print("1) Aşağıdakilerden hangisi Türkiye'nin en büyük dağıdır?")
print("A) Erciyes")
print("B) Ağrı")
print("C) Ilgaz")
print("D) Toroslar")
cevap=input("Cevabınız:")
if(cevap=="B" or cevap=="b"):
    print("Cevabınız doğru, tebrikler.")
    puan=puan+10
else:
    print("Cevabınız yanlış, doğru cevap B olacaktı")

print("2) Aşağıdakilerden hangisi Türkiye'nin en büyük gölüdür?")
print("A) Tuz")
print("B) Beyşehir")
print("C) Van")
print("D) Eğirdir")
cevap=input("Cevabınız:")
if(cevap=="C" or cevap=="c"):
    print("Cevabınız doğru, tebrikler.")
    puan=puan+10
else:
    print("Cevabınız yanlış, doğru cevap C olacaktı")
print("Puanınız:",puan)
