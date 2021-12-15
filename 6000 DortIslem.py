from tkinter import *


class MyWindow:
    def __init__(self, win):

        self.lbl1 = Label(win, text='Birinci Sayı')
        self.lbl2 = Label(win, text='İkinci Sayı')
        self.lbl3 = Label(win, text='Sonuç')

        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()



        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.b1 = Button(win, text='Ekle', command=self.ekle)
        self.b2 = Button(win, text='Çıkar', command=self.cikar)
        self.b3 = Button(win, text='Çarp', command=self.carp)
        self.b4 = Button(win, text='Böl', command=self.bol)

        # self.b2.bind('<Button-1>', self.cikar)
        self.b1.place(x=100, y=150)
        self.b2.place(x=150, y=150)
        self.b3.place(x=200, y=150)
        self.b4.place(x=250, y=150)

        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def ekle(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def cikar(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def carp(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def bol(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        if (num2 != 0):
            result = num1 / num2
            self.t3.insert(END, str(result))
        else:
            self.t3.insert(END, "Tanımsız")


window = Tk()
mywin = MyWindow(window)
window.title('Tkinter Dört İşlem')
window.geometry("400x300+10+10")
window.mainloop()