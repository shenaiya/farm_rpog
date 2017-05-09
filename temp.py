import sqlite3
from tkinter import *
from tkinter.ttk import *

root = Tk()
con = sqlite3.connect('farm.db')
cur = con.cursor()
cur1 = con.cursor()
derevo = Treeview(root)
derevo["columns"] = ("one")
derevo.column("#0", width=40)
derevo.column("one", width=40)
derevo.heading("#0", text="Хрень")
derevo.heading("one",text="Хрень1")
def search(A, key):
    for i in range(len(A)):
        if A[i] == key:
           return True
    return False


def all2():
    e = cur.execute('select vid_animal.id, vid_animal.vid_name from vid_animal join animal on animal.id_vid where animal.id_vid=vid_animal.id')
    mas = [58, 48, 16]
    for dd in e:
        p = search(mas,dd[0])
        if p:
            print(p,"1")
        else:
            derevo.insert("", 1, dd[0], text=dd[1])
            mas.insert(0,dd[0])
            isk = dd[0]
            print(isk)
            k = cur1.execute("select animal.id, animal.name from animal where animal.id_vid=%s" % isk)
            for ddd in k:
                derevo.insert(dd[0], 3, text=ddd[1] )
                print ([ddd[0],ddd[1]],"2")



derevo.pack()
derevo.place(x=10, y=100, width=230, height=490)
object = all2()
root.minsize(1024, 600)
root.mainloop()
