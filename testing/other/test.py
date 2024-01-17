import tkinter as tk
from tkinter import ttk
import random

colors = [
    "black", "dimgray", "gray", "darkgray", "silver", "lightgrey", "gainsboro", "whitesmoke", "white", "snow",
    "rosybrown", "lightcoral", "indianred", "brown", "firebrick", "maroon", "darkred", "red", "mistyrose", "salmon",
    "tomato", "darksalmon", "coral", "orangered", "lightsalmon", "sienna", "seashell", "saddlebrown", "chocolate",
    "sandybrown", "peachpuff", "peru", "linen", "bisque", "darkorange", "burlywood", "tan", "antiquewhite",
    "navajowhite", "blanchedalmond", "papayawhip", "moccasin", "orange", "wheat", "oldlace", "floralwhite",
    "darkgoldenrod", "goldenrod", "cornsilk", "gold", "lemonchiffon", "khaki", "palegoldenrod", "darkkhaki", "ivory",
    "beige", "lightyellow", "lightgoldenrodyellow", "olive", "yellow", "olivedrab", "yellowgreen", "darkolivegreen",
    "greenyellow", "chartreuse", "lawngreen", "honeydew", "darkseagreen", "palegreen", "lightgreen", "forestgreen",
    "lime", "seagreen", "mediumseagreen", "springgreen", "mintcream", "mediumspringgreen", "mediumaquamarine",
    "aquamarine", "turquoise", "lightseagreen", "mediumturquoise", "azure", "lightcyan", "paleturquoise",
    "darkslategray", "teal", "darkcyan", "aqua", "cyan", "darkturquoise", "cadetblue", "powderblue", "lightblue",
    "deepskyblue", "skyblue", "steelblue", "aliceblue", "dodgerblue", "lightslategray", "slategray", "royalblue",
    "ghostwhite", "lavender", "midnightblue", "navy", "blue", "cornflowerblue", "darkslateblue", "slateblue",
    "mediumblue", "blueviolet", "indigo", "darkorchid", "darkviolet", "mediumorchid", "thistle", "plum", "violet",
    "purple", "darkmagenta", "orchid", "mediumpurple", "mediumslateblue", "lavenderblush", "crimson", "fuchsia",
    "hotpink", "deeppink", "pink", "lightpink", "palevioletred", "mediumvioletred", "slategray"
]


def on_button_click(dropdowns):
    # Update the list with desired values
    result_list.clear()
    for item in dropdowns:
        result_list.append(item.get())  # Replace this with your actual values
    print("Button Clicked")
    print("Result List:", result_list)


root = tk.Tk()
root.title("Button Example")

result_list = []

dropdowns = []
for x in range(3):
    dropdown = ttk.Combobox(root, values = colors, state='readonly')
    dropdown.grid(row=2, column=x, padx=10)
    dropdowns.append(dropdown)

button = tk.Button(root, text="Click Me", command=lambda: on_button_click(dropdowns))
button.grid()

root.mainloop()

# After the main loop, you can access the updated list
