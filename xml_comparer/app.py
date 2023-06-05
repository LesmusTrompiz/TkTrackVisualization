from controller.main_controller import MainController
from views.main_view import MainView
from tkinter import Tk, PhotoImage
from tkinter.ttk import Label, Frame



if __name__ == "__main__":
    root = Tk("Comparador de XMLS")
    main_view = MainView(root)

    
    main_controller = MainController(main_view)
    title_frame = Frame(root, relief='ridge', borderwidth=10)
    label = Label(root, text="COMPARADOR DE XMLS", font={'size' :20})
    label.grid(row=0, column=0, sticky='NS')#, padx = main_view.winfo_screenwidth()/2)
    
    
    image_label =  Label(root)
    image = PhotoImage(file='D:/Proyectos/TkTrackVisualization/xml_comparer/ex.png',width=30, height=30)
    image_label['image'] = image
    
    
    image_label.grid(row=0, column=1, sticky='NSEW')
    title_frame.grid(row=0, column=0,  sticky='NSEW')
    
    main_view.grid(row=1, column=0, sticky='NSEW')
    root.columnconfigure(0,weight=1)
    root.rowconfigure(1,weight=10)
    root.rowconfigure(0,weight=1)
    print(main_view.winfo_screenwidth())
    root.mainloop()
    