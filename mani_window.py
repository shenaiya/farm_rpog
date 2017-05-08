# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *


class main_bitton:
    def __init__(self):
        self.size = [10, 90, 170, 250, 330]  # кооржинаты расположения кнопок по х
        self.but = [0, 1, 2, 3, 4]  # добавка к имени кнопки
        self.nadpis = ["Коноака0", "Кнопка1", "Кнопка2", "Кнопка3", "Кнопка4"]  # отображаемая надпись на кнопке
        self.img = PhotoImage(file="stat.png")  # подгрузка картинки
        for xx in self.but:  # цикл генерирующий кнопки
            self.but[xx] = Button(root, text=self.nadpis[xx], image=self.img)
            self.but[xx].bind("<Button-1>", self.pod)
            self.but[xx].pack()
            self.but[xx].place(x=self.size[xx], y=10, width=70, height=70)
        self.labla = Label(root, text="Живность")  # нажпись
        self.labla.pack()
        self.labla.place(x=10, y=80)
        self.style = Style()

        self.derevo = Treeview(root)
        def OnDoubleClick(event):
            item = self.derevo.identify('item', event.x, event.y)
            print("you clicked on", self.derevo.item(item, "text"))
        self.derevo.bind('<Button-1>', OnDoubleClick)
        self.derevo["columns"] = ("one", "two")
        self.derevo.column("#0", width=40)
        self.derevo.column("one", width=40)
        self.derevo.column("two", width=40)
        self.derevo.heading("#0", text="Хрень")
        self.derevo.heading("one", text="coulmn A")
        self.derevo.heading("two", text="column B")
        self.derevo.insert("", 0, text="Line 1", values=("1A", "1b"))
        self.id2 = self.derevo.insert("", 1, "dir2", text="Dir 2")
        self.derevo.insert(self.id2, "end", "dir 2", text="sub dir 2", values=("2A", "2B"))
        self.derevo.insert("", 3, "dir3", text="Dir 3")
        self.derevo.insert("dir3", 3, text=" sub dir 3", values=("3A", " 3B"))
        self.derevo.pack()
        self.derevo.place(x=10, y=100, width=230, height=490)

    def pod(self, event):
        print("Привет новый мир")


root = Tk()
root.minsize(1024, 600)
object = main_bitton()
root.mainloop()
