from tkinter import *
class MyWindow:
    def __init__(self, win):

        self.lbl1=Label(win, text='Adınız:')
        self.t1=Entry()
        self.t2=Entry()


        self.lbl1.place(x=50, y=50)
        self.t1.place(x=150, y=50)
        self.t2.place(x=150, y=100)
        self.b1=Button(win, text='Giriş', command=self.mrb)
        self.b1.place(x=150, y=70)

    def mrb(self):
        self.t2.delete(0, 'end')
        adi=self.t1.get()
        self.t2.insert(END, "Merhaba "+adi+" Hoş geldiniz")




window=Tk()
mywin=MyWindow(window)
window.title('Merhaba')
window.geometry("400x200+10+10")
window.mainloop()