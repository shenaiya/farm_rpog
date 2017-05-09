from tkinter import *

class main_window:
    def __init__(self):
        self.text = Entry(window, width=20)
        self.text.pack()
        self.button = Button(window, text="Config")
        self.button.bind("<Button-1>", self.list)
        self.button.pack()

    def conf(self,event):
        win = Toplevel(window, relief=SUNKEN, bd=10, bg="lightblue")
        win.title("Дочернее окно")
        win.minsize(width=400, height=200)
    def list(self,event):
        r = ['Linux', 'Python', 'Tk', 'Tkinter']
        lis = Listbox(window, selectmode=SINGLE, height=4)
        for i in r:
            lis.insert(END, i)
        lis.pack()
window = Tk()
object = main_window()
window.mainloop()
