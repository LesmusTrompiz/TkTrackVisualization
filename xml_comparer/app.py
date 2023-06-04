from controller.main_controller import MainController
from views.main_view import MainView
from tkinter import Tk
from tkinter.ttk import Label



if __name__ == "__main__":
    root = Tk()
    main_view = MainView(root)

    
    main_controller = MainController(main_view)
            
    label = Label(root, text="COMPARADOR DE XMLS")
    label.grid(row=0, column=0, sticky='NSEW')
        
    
    
    main_view.grid(row=1, column=0,sticky='NSEW')
    root.columnconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.mainloop()
    