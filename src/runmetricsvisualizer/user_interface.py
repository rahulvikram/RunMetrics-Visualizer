# initialize tkinter ui
# function will return parameters for plot() functionality
import csv
import tkinter as tk
import random
from PIL import ImageTk, Image
from tkinter import ttk
from runmetricsvisualizer.helpers import *
import runmetricsvisualizer.plot

# end variables to return
# chart style
chart_style, plot_type, title = 'default', 'scatter', 'X vs Y'

def get_settings(color_inputs, plottype_var, chartbg_var, title_var, plot_file):    
    items = []
    # STEP 1: return all point colors as a list:
    for item in color_inputs:
        if not item.get(): # if a color field is left blank
            items.clear() # empty items list, break out of loop
            break
        items.append(item.get()) # otherwise, add it to new items list

    # if user colors were added, replace colors list
    if len(items) > 0:
        point_colors.clear()
        for color in items:
            point_colors.append(color)

    # return other vars
    plot_type, chart_style, title = plottype_var.get(), chartbg_var.get(), title_var.get()


    # run plot function from timer.py at the end using all modified variables
    plot.generate_plot(plot_file, plot_type, chart_style, title, point_colors)

def initialize_ui(plot_file):

    with open(plot_file, 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        functions = next(rows)
        functions.pop(0)

    # initializes point colors to randomc colors incase user leaves fields blank
    global point_colors 
    point_colors = random.sample(colors, len(functions))

    # Window title
    root = tk.Tk()
    root.title("Function Graphing GUI")

    # section 1: Color dorpdown menus
    # dropdown section title
    label = tk.Label(root, text='Function Colors', font=('Helvetica', 12, 'bold'))
    label.grid(row=0, column=1)

    color_inputs = [] # empty color_inputs
    for z in range(len(functions)):
        # generate a dropdown box for function
        dropdown = ttk.Combobox(root, values = colors, state='readonly')
        dropdown.grid(row=2, column=z, padx=10, pady=(2, 8))
        color_inputs.append(dropdown)

        # dropdown labels above each dropdown, corresponding to function name
        label = tk.Label(root, text=functions[z], font=('Helvetica', 11))
        label.grid(row=1, column=z, padx=10)


    # section 2: Plot type choices
    # plot type section title
    label = tk.Label(root, text='Plot Type', font=('Helvetica', 12, 'bold'))
    label.grid(row=3, column=1, pady=(12, 0))

    # set images for radiobuttons
    image = tk.PhotoImage(file='src/img/plot-types/scatter.png')
    scatter_img = image.subsample(4,4)
    image = tk.PhotoImage(file='src/img/plot-types/lineplot.png')
    lineplot_img = image.subsample(5,5)
    image = tk.PhotoImage(file='src/img/plot-types/stackplot.png')
    stackplot_img = image.subsample(4,4)

    # radio buttons for selections
    i = tk.StringVar() #Basically Links Any Radiobutton With The Variable=i.
    scatterplot = ttk.Radiobutton(root, image=scatter_img, text='scatter', value='scatter', variable=i, takefocus=False)
    lineplot = ttk.Radiobutton(root, image=lineplot_img, text='line plot', value='plot', variable=i, takefocus=False)
    stackplot = ttk.Radiobutton(root, image=stackplot_img, text='stackplot', value='stackplot', variable=i, takefocus=False)
    
    scatterplot.grid(row=4, column=0, padx= 5)
    lineplot.grid(row=4, column = 1, padx= 5)
    stackplot.grid(row=4, column=2, padx= 5)


    # section 3: chart background
    # plot type section title
    label = tk.Label(root, text='Chart Background', font=('Helvetica', 12, 'bold'))
    label.grid(row=5, column=1, pady=(12, 0))

    # set images for radiobuttons
    image = tk.PhotoImage(file='src/img/backgrounds/defaultbg.png')
    default = image.subsample(4,4)
    image = tk.PhotoImage(file='src/img/backgrounds/darkbg.png')
    dark = image.subsample(4,4)
    image = tk.PhotoImage(file='src/img/backgrounds/solarizedbg.png')
    solarized = image.subsample(4,4)

    # radio buttons for selections
    j = tk.StringVar() #Basically Links Any Radiobutton With The Variable=i.
    defaultbg = ttk.Radiobutton(root, image=default, value='default', variable=j, takefocus=False)
    darkbg = ttk.Radiobutton(root, image=dark, value='dark_background', variable=j, takefocus=False)
    solarizedbg = ttk.Radiobutton(root, image=solarized, value='Solarize_Light2', variable=j, takefocus=False)
    
    defaultbg.grid(row=6, column=0, padx= 5)
    darkbg.grid(row=6, column = 1, padx= 5)
    solarizedbg.grid(row=6, column=2, padx= 5)


    # section 4: chart title section
    label = tk.Label(root, text='Chart Title', font=('Helvetica', 12, 'bold'))
    label.grid(row=7, column=1, pady=(12, 0))

    # input widget
    k = tk.StringVar()
    entry = tk.Entry(root, textvariable=k)
    entry.grid(row=8, column=1, pady=(0, 10))


    # FINAL: on button click, for each setting, whatever its currently selecting, it will return those as variables via command
    submit = tk.Button(root, text = 'Generate Graph!!', font=('Helvetica', 14, 'bold'),command=lambda: get_settings(color_inputs, i, j, k, plot_file))
    submit.grid(row=10, column=1, pady=(0, 10))

    # display UI on screen
    root.mainloop()