from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)



class Scenario_value:
    def __init__(self, parent, name, coords, value_ranges) -> None:
        x, y = coords
        min, max = value_ranges
        variable_label = Label(parent, text=name+": " )
        variable_label.grid(column=x, row=y, padx=5, pady=5)


        self.min_value = min
        self.max_value = max
        self.variable = StringVar()

        check_variable_limits = (parent.register(self.check_limit), '%P', '%V')
        variable_entry = ttk.Entry(parent, textvariable=self.variable, validate='all', validatecommand=check_variable_limits)
        variable_entry.grid(column=x + 1, row=y, padx=5, pady=5)
        variable_slider = ttk.Scale(parent, orient=HORIZONTAL, length=200, from_=min, to=max, variable=self.variable)
        variable_slider.grid(column=x + 2, row = y, padx = 5, pady = 5)

    def check_limit(self, new_value, event_type):
        err = ""
        if not new_value: return True

        try:
            errmsg.set(err)
            number_value = float(new_value)
        except:
            errmsg.set("Not a valid number")
            return False
        
        if event_type == "key": 
            if number_value >= float(self.max_value):
                errmsg.set("Valor por encima del máximo")
                self.variable.set(self.max_value)
                return False
            return True
        
        if number_value > float(self.max_value):
            errmsg.set("Valor por encima del máximo")
            self.variable.set(self.max_value)
            return False
        elif number_value < float(self.min_value):
            errmsg.set("Valor por debajo del mínimo")
            self.variable.set(self.min_value)
            return False
        return True


if __name__ == "__main__":
    root = Tk()
    root.title("Scenario")
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    ax = fig.add_subplot()
    line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
    ax.set_xlabel("time [s]")
    ax.set_ylabel("f(t)")



    
    f = ttk.Frame(root)
    f.grid(column=0, row=0)
    
    canvas = FigureCanvasTkAgg(fig, master=f)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()


    scenario_values = [('range', 0, 100), ('range2', 20, 200), 
                       ('range3', 30, 300), ('range4', 40, 400),
                       ('range5', 50, 500), ('range6', 60, 600),
                       ('range7', 70, 700), ('range8', 80, 800),
                       ('range5', 90, 900)]
    
    n = 0
    for value in scenario_values:
        name, min_range, max_range = value
        Scenario_value(f, name, ((n%2)*3, int(n/2)), (min_range, max_range))
        n+=1

    errmsg = StringVar()
    msg = ttk.Label(f, font='TkSmallCaptionFont', foreground='red', textvariable=errmsg)
    msg.grid(column=3, row=8)
    canvas.get_tk_widget().grid()
    root.mainloop()


