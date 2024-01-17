# initialize tkinter ui
# function will return parameters for plot() functionality
import csv
import tkinter as tk
from tkinter import ttk
from helpers import *

# end variables to return
# chart style
# plot type
# title
point_colors = [] # point colors


def get_settings(dropdowns):    
    # run plot function from timer.py at the end

    # step 1: g
    point_colors.clear()
    for item in dropdowns:
        point_colors.append(item.get())

def initialize_ui(file):
    with open(file, 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        functions = next(rows)
        functions.pop(0)
    
    root = tk.Tk()

    root.configure(background='#030303')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TCombobox', fieldbackground='#d6d6d6')


    # section 1: DISPLAY the dropdown menus onscreen
    dropdowns = [] # empty dropdowns
    for function in functions: # for each function that exists
        # generate a dropdown box for function
        dropdown = ttk.Combobox(root, values = colors, state='readonly')
        dropdown.grid(row=2, column=functions.index(function), padx=10, pady=(2, 8))
        dropdowns.append(dropdown)

        # TODO: Add dropdown labels above each dropdown, corresponding to function name
        label = tk.Label(root, text=function)
        label.grid(row=1, column=functions.index(function), padx=10)

    
    
    # FINAL: on button click, for each setting, whatever its currently selecting, it will return those as variables via command
    submit = tk.Button(root, text = 'testing this out', bd='5', command=lambda: btn_test(dropdowns))
    submit.grid(row=3, column=1)


    # display UI on screen
    root.wm_attributes('-transparentcolor','black')
    root.mainloop()




initialize_ui('data/first_test.csv')