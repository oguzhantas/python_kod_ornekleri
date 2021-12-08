# 0 ve sıfırın altında ise su donar, katı haldedir
# 1 ve 99 derece(99 dahil) arasında ise sıvı haldedir
# 100 derece ve üstü ise su buharlaşır, gaz halindedir

s = int(input("Sıcaklık giriniz:"))

if(s<=0):
    print("Su donmuş, katı halde")

elif(s>0 and s<100): # 0 ile 100 arasında
    print("Sıvı halde, akıcı")

elif(s>=100):
    print("Gaz halinde, su buharlaşıyor")