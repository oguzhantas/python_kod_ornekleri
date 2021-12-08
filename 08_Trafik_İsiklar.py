renk=input("Işık rengini giriniz(K/Y/S):")

if (renk=='K' or renk=='k'):
    print("Kırmızı ışık, lütfen durunuz.")

elif(renk=='S' or renk=='s'):
    print("Sarı ışık, lütfen bekleyiniz.")

elif(renk=='Y' or renk=='y'):
    print("Yeşil Işık, geçebilirsiniz.")

else:
    print("Lütfen K/Y/S harflerinden birini giriniz.")