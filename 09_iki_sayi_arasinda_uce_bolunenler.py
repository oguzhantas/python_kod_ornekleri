#iki sayı arasında üçe bölünenleri bulma
s1= int(input("1. sayıyı giriniz:"))  #5 olsun
s2= int(input("2. sayıyı giriniz:"))  #10 olsun

i=s1
while(i<=s2):
    if (i%3==0):
        print(i)
    i=i+1