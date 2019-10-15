from tkinter import *


root = Tk()

class Frames:
    def __init__(self,master):
        self.master = master
        f1 = Frame(master)
        f1.pack()


        self.f2 = Frame(self.master)
        self.f2.pack()

        self.b1 = Button(f1,text="Frame1button",fg="red",command=self.f2.forget) 
        self.b1.pack()

        self.b2 = Button(f1,text="Get back",command=self.getback)
        self.b2.pack()

        self.l1 = Label(self.f2,text="FRAME2")
        self.l1.pack()

    def hide1(self):
        self.f2.withdraw()

    def getback(self):
        self.f2.pack()

obj = Frames(root)

root.mainloop()

        
        
