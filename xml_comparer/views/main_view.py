from tkinter import Tk
from tkinter.ttk import  Frame, Treeview, Label, Button, Scrollbar



class SelectXMLView(Frame):
    def __init__(self, master: Frame, file_number: int):
        Frame.__init__(self, master)
        self.label_title = Label(self, text=f"Fichero {file_number}")
        self.button_select = Button(self, text=f"Seleccionar el fichero {file_number}")
        self.tree_view = Treeview(self)
        right_scrollbar = Scrollbar(self, orient = 'vertical', command = self.tree_view.yview )  
        low_scrollbar = Scrollbar(self, orient = 'horizontal', command = self.tree_view.xview )  
        
        self.label_title.grid(row=0, column=0)
        self.button_select.grid(row=1, column=0)
        self.tree_view.grid(row=2, column=0, sticky='NSEW', padx=15, pady=15)
        right_scrollbar.grid(column=0, row=2, sticky='nse')
        low_scrollbar.grid(column=0, row=2, sticky='swe', padx=15)
        
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        
        
class OutputComparedView(Frame):
    def __init__(self, master: Frame, file_number: int):
        Frame.__init__(self, master)
        self.label_title = Label(self, text=f"Fichero de Salida {file_number}")
        self.button_select = Button(self, text=f"Comparar ficheros {file_number}")
        self.tree_view = Treeview(self)
        
        right_scrollbar = Scrollbar(self, orient = 'vertical', command = self.tree_view.yview )  
        low_scrollbar = Scrollbar(self, orient = 'horizontal', command = self.tree_view.xview )  
        
        
        self.label_title.grid(row=0, column=0)
        self.button_select.grid(row=1, column=0)
        self.tree_view.grid(row=2, column=0, sticky='NSEW', padx=15, pady=15)
        right_scrollbar.grid(column=0, row=2, sticky='nse')
        low_scrollbar.grid(column=0, row=2, sticky='swe', padx=15)
        
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        
        
class MainView(Frame):
    def __init__(self, master: Tk):
        Frame.__init__(self, master)
        
        self.frame_f1 = SelectXMLView(self, 1)
        self.frame_f2 = SelectXMLView(self, 2)
        self.frame_f3 = OutputComparedView(self, '1-2')
        self.frame_f4 = OutputComparedView(self, '2-1')
        
        
        # 
        self.frame_f1.grid(row=0, column=0, sticky='NSEW')
        self.frame_f2.grid(row=0, column=1, sticky='NSEW')
        self.frame_f3.grid(row=0, column=2, sticky='NSEW')
        self.frame_f4.grid(row=0, column=3, sticky='NSEW')
        
        
        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        



if __name__ == "__main__":
    root = Tk()
    view = MainView(root).grid(row=0, column=0)
    view.rowconfigure(0, row=0)
    view.columnconfigure(0, column=0)
    view.columnconfigure(0, column=1)
    
    
    root.mainloop()
    
    
    