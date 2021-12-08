#1 ile 100 arasında 3 ve 5'e aynı anda bölünen sayıları yazınız
# 15, 30, 45, 60, 75, 90
i=0
while i<100:
    i+=1
    if (i%3==0 and i%5==0):
        print(i)

