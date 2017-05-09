import sqlite3
from tkinter import *

root = Tk()
size = [10, 90, 170, 250, 330]  # кооржинаты расположения кнопок по х
con = sqlite3.connect('farm.db')
cur = con.cursor()
t = cur.execute('SELECT * from enimal')
#for name in cur.execute('SELECT name from enimal'):
#        for id in cur.execute('SELECT id from enimal'):

def pod(event):
    print("Привет новый мир")

for xx in t:
        #but = "but"
        #but = but + xx[1]
        but = Button(root, text=xx[1])
        print (but)
        but.bind("<Button-1>",pod)
        but.pack()
        but.place(x=size[xx[0]], y=10, width=70, height=70)


root.mainloop()