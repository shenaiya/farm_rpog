import sqlite3
from tkinter import *
from tkinter.ttk import *

root = Tk()
size = [10, 90, 170, 250, 330]  # кооржинаты расположения кнопок по х
con = sqlite3.connect('farm.db')
cur = con.cursor()
#for name in cur.execute('SELECT name from enimal'):
#        for id in cur.execute('SELECT id from enimal'):
derevo = Treeview(root)

def pod(event):
    print("Привет новый мир")
def all ():
        t = cur.execute('SELECT * from animal')
        for xx in t:
                but = Button(root, text=xx[1])
                print (xx)
                but.bind("<Button-1>",pod)
                but.pack()
                but.place(x=size[xx[0]], y=10, width=70, height=70)

def all2 ():
        e = cur.execute('SELECT * from animal')
        for dd in e:
                print (dd[1])
                derevo.insert("", "end", dd[0], text=dd[1], values=("2A", "2B"))
                derevo.pack()
                derevo.place(x=10, y=100, width=230, height=490)


object = all()
object = all2()
root.minsize(1024, 600)
root.mainloop()