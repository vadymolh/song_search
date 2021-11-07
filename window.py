from tkinter import *


class Window(Tk):
    def ___init__(self):
        super().__init__()
        Label(text="Введіть пошуковий запит:").grid(
           row = 0, column=0, columnspan=2 
        )
        

if __name__=="__main__":
    root = Window()
    root.geometry("300x200")
    root.mainloop()