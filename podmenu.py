from tkinter import *
from tkinter import messagebox

class MenuBar(Menu):
    def __init__(self, ws):
        Menu.__init__(self, ws)

        file = Menu(self, tearoff=False)
        file.add_command(label="Nowa karta")  
        file.add_command(label="Nowe okno")  
        file.add_command(label="Otwórz")  
        file.add_command(label="Zapisz")    
        file.add_separator()
        file.add_command(label="Wyjdź", underline=1, command=self.quit)
        self.add_cascade(label="Plik",underline=0, menu=file)
        

class MenuDemo(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    ws=MenuDemo()
    ws.title('menu')
    ws.geometry('500x400')
    ws.mainloop()
