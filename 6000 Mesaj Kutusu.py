from tkinter import *

pencere = Tk()
pencere.title('Mesajınız var!')
pencere.geometry('400x300')
pencere.config(bg='#299F04')

mesaj ='''
 Sayın Kullanıcı,

  1) İşletim Sistemini güncelleyiniz.
  2) Antivirüs yazılımı kurunuz.
  3) Antivirüs yazılımını güncelleyiniz.
  4) Ara ara yedekleme yapınız.

 Teşekkürler,
 Bilgi İşlem '''

tbox = Text(pencere, height=12, width=40)
tbox.pack(expand=True)
tbox.insert('end', mesaj)
tbox.config(state='disabled')

pencere.mainloop()