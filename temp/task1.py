# -*- coding: utf-8 -*-
from tkinter import *

class adress:
    def __init__(self):
        self.label = Label(window, text="Ваш адрес:", font="Arial 14", bg="yellow")
        self.text = Entry(window,width=20,bd=3)


        self.label1 = Label(window, text="Комментарий:", font="Arial 10")
        self.text_field = Text(window, width=20, height=10,
                         font="Verdana 12",
                         wrap=WORD)  # перенос по словам
        self.button = Button(window,  # Объявляем кнопку и её переменные
                             text="Отправить",  # имя кнопки
                             width=15, height=2,  # размер кнопки
                             bg="Steel Blue", fg="black")  # цвет фона и текста
        self.label.pack()
        self.text.pack()
        self.label1.pack()
        self.text_field.pack()
        self.button.pack()
window = Tk()
object = adress()
window.mainloop()