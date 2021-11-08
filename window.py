#-*- codding:utf-8 -*-
from tkinter import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        Label(self ,text="Введіть пошуковий запит:").grid(
           row = 0, column=0, columnspan=2 
        )
        self.search_text = StringVar()
        self.entry_search = Entry(self, width=60, 
                                  textvariable=self.search_text)
        self.search_but = Button(self, text="Пошук",
                                 command=self.search)
    def search(self):
        print("Text from entry:",self.search_text.get())

if __name__=="__main__":
    root = Window()
    root.geometry("300x200")
    root.mainloop()