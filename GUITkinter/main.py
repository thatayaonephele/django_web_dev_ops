from tkinter import *
import math
from tkinter import  ttk
def volume():
    v, r = 1, 2
"""
#Programming Exercises:

def volume_of_circle():
    
    try:
        value = float(r.get())
        v.set(4/3 * math.pi * math.pow(value, 3), 2) #1 Calculate Volume & SA:
#        sa = round(4 * math.pi * math.pow(r, 2), 2)
        print("The volume of a circle with radius {} is {}m^3".format(value, v))
#        print("The Surface Area of a circle with radius {} is {}m^2".format(r, sa))
    except ValueError:
        pass

def calulate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 1000.0  + 0.5)/10000.0)
    except ValueError:
        pass"""

root = Tk()
root.title("E-Learning")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

"""feet = StringVar()
meters = StringVar()
r =StringVar()
"""

feet_entry = ttk.Entry(mainframe, width=7)
feet_entry.grid(column=2, row=2, sticky=(W,E))

ttk.Button(root, text="Refresh").grid()
ttk.Button(root, text="Calculate").grid()
ttk.Button(root, text="Exit").grid()

ttk.Label(mainframe, text="please enter a radius value: ").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="The volume of a circle with radius {} is {}m^3".format(r, v)).grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', volume())

root.mainloop()


#calulate()