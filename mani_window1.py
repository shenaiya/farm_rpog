# -*- coding: utf-8 -*-
from tkinter import *
from sys import maxsize
from ctypes.test.test_pickling import name


class main_bitton:
    def __init__(self):
        self.size = [10,90,170,250,330]  #кооржинаты расположения кнопок по х
        self.but = [0,1,2,3,4]           #добавка к имени кнопки
        self.nadpis = ["Коноака0","Кнопка1","Кнопка2","Кнопка3","Кнопка4"] #отображаемая надпись на кнопке
        self.img = PhotoImage(file="stat.png")  #подгрузка картинки
        for xx in self.but: #цикл генерирующий кнопки
            self.but[xx] = Button(root, text = self.nadpis[xx],image=self.img)
            self.but[xx].bind("<Button-1>",self.pod)
            self.but[xx].pack()
            self.but[xx].place(x=self.size[xx], y=10, width=70, height=70)    
        self.labla = Label(root, text = "Живность") #нажпись 
        self.labla.pack()
        self.labla.place(x=10, y=80)
        def onselect(evt): #эвент выбора части списка
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            print ("You selected item %d: %s"% (index, value))
        self.r = ['КУры','Овцы','Кролики','мышы'] #список строк 
        self.list = Listbox(root)
        for i in self.r: #собирает строки из списка 
            self.list.insert(END,i)
        self.list.bind('<<ListboxSelect>>',  onselect) #процедура нажатия 
        self.list.pack()
        self.list.place(x=10, y=100, width=230, height=500)
    def pod(self,event):
        print ("Привет новый мир")
    


root = Tk()
root.minsize(1024, 600)
object = main_bitton()
root.mainloop()