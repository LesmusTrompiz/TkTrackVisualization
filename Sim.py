from threading import Thread, Lock
from time import sleep
from tkinter import *
from tkinter import ttk
from typing import Dict, List
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np



def increment_x(scenario):
    scenario['x'] = scenario['x'] + 10
    return scenario


class FigPlot:
    def __init__(self, parent) -> None:
        fig = Figure()
        self.ax = fig.add_subplot()
        self.ax.plot([0, 10], [0, 5])
        self.canvas = FigureCanvasTkAgg(fig, master=parent)  # A tk.DrawingArea.
        self.canvas.draw()

    def draw(self, x) -> None:
        self.ax.clear()
        self.ax.plot([x, x], [0, 5])
        self.canvas.draw()
        
        
        
class Sim(Thread):
    def __init__(self, funcs: List, tk_variables: Dict[str, StringVar]) -> None:
        Thread.__init__(self, daemon=True)

        self.ts = 0.5
        self.funcs  = funcs

        self.sim_scenario = {}
        
        self.lock_scenario = Lock()
        
        self.lock_output = Lock()
        
        self.output_scenario = {}
        self.output_flag = BooleanVar()

        for key in tk_variables.keys():
            self.sim_scenario[key] = float(tk_variables[key].get())

    def change_sim_scenario(self, new_scenario):
        self.lock_scenario.acquire()
        for key in new_scenario.keys():
            self.sim_scenario[key] = new_scenario[key]
        self.lock_scenario.release()
            
    def run(self):
        while True:
            self.lock_scenario.acquire()
            for func in self.funcs:
                self.sim_scenario = func(self.sim_scenario)
            self.lock_scenario.release()
            self.update_output()
            sleep(self.ts)

    def update_output(self):
        self.lock_output.acquire()
        for key in self.sim_scenario.keys():
            self.output_scenario[key] = float(self.sim_scenario[key])
        self.lock_output.release()
        self.output_flag.set(True)
        
        
        
def sim_update(*args):
    s.lock_output.acquire()
    x_plot.draw(float(s.output_scenario["x"]))
    x.set(s.output_scenario["x"])
    s.lock_output.release()
    

def update_x(*args):
    new_scenario = {}
    new_scenario['x'] = float(tk_variables['x'].get())
    s.change_sim_scenario(new_scenario)
    

if __name__ == "__main__":
    # 
    root = Tk()
    root.title("Scenario")

    # Variable utilizada para el label
    x = StringVar()
    x.set('1')
    
    tk_variables = {}
    tk_variables['x'] = x

    

    x_sim_label = Label(root, textvariable=x).grid(row=0, column=0)
    x_entry = Scale(root, variable=x, command=update_x).grid(row=1, column=0)
    x_plot = FigPlot(root)
    x_plot.canvas.get_tk_widget().grid(column=0,row=2)
    

    s = Sim([increment_x], tk_variables)
    s.output_flag.trace_add("write", sim_update)
    s.start()

    root.mainloop()
