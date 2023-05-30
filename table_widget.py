from tkinter.ttk import Label, Entry, Frame
from tkinter import Widget, Tk, END
from typing import List
from pandas import read_excel

class Table(Frame):
    def __init__(self, parent : Widget):
        Frame.__init__(self, parent)
        self.__rows_number = 0
        self.__columns_number = 0
        self.__columns_names = {}
        self.cells = []
        
        self.add_column_index('index')

    def add_row(self, data: List, resize=False):
        self.__rows_number += 1
        
        if len(data) > self.__columns_number:
            self.__columns_number = len(data) + 1
        
        e = Entry(self, width=10, foreground='blue')
        e.grid(row=self.__rows_number, column=0)
        e.insert(END, str(self.__rows_number) )
        r = [e]
        
        for column in range(1, self.__columns_number):
            e = Entry(self, width=20)
            e.grid(row=self.__rows_number, column=column)
            e.insert(END, str(data[column - 1]))
            r += [e]
            
        self.cells += [r]
    
    def add_column_index(self, name: str, resize=False):
        self.__columns_names[name] = self.__columns_number
        
        e = Entry(self, width=10, foreground='blue')
        e.grid(row=0, column=self.__columns_number)
        e.insert(END, name)
        if self.cells:
            self.cells[0] += [e]
        else:
            self.cells += [[e]]
        
        self.__columns_number += 1
        
        
        
        
        
        
        


if __name__ == "__main__":
    root = Tk()    
    df = read_excel("./Libro1.xlsx")
    df.dropna(how='all', axis=1, inplace=True)
    d = df.dropna()
    d = d.reset_index(drop=True)
    d = d.set_axis(d.iloc[0],axis='columns' )
    d = d.iloc[1:]
    print(d)
    t = Table(root)
    t.grid(row=0,column=0)
    for c in range(4):
        data = [n for n in range(3)]
        t.add_row(data)
    
    root.mainloop()