from controller.main_controller import MainController
from views.main_view import MainView
from tkinter import Tk, PhotoImage, Label
from tkinter.ttk import  Frame



if __name__ == "__main__":
    root = Tk("Comparador de XMLS")
    main_view = MainView(root)

    
    main_controller = MainController(main_view)
    title_frame = Frame(root, relief='ridge', borderwidth=10)
    
    label = Label(title_frame, text="COMPARADOR DE XMLS", font={'size' :30})
    
    
    image_label =  Label(title_frame, width=300,  height=150)
    image = PhotoImage(file='D:/Proyectos/TkTrackVisualization/xml_comparer/ex2.png')#,width=100, height=200)
    image_label['image'] = image
    
    image_label.grid(row=0, column=3)
    label.grid(row=0, column=0, sticky='NS')#, padx = main_view.winfo_screenwidth()/2)
    
    
    
    
    title_frame.grid(row=0, column=0,  sticky='NSEW')
    
    title_frame.columnconfigure(0,weight=1)
    title_frame.rowconfigure(0,weight=1)
    
    
    
    main_view.grid(row=1, column=0, sticky='NSEW')
    root.columnconfigure(0,weight=1)
    root.rowconfigure(1,weight=10)
    #root.rowconfigure(0,weight=1)
    root.update_idletasks() 
    print(image_label.winfo_width())
    image_label.winfo_height
    
    print(main_view.winfo_screenwidth())
    root.mainloop()
    