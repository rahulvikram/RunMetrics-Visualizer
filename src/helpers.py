"""These are helper functions and variables designed to make the class code less cluttered."""
import time

# splits the output string into separate file and folder strings
def split_output(string):
    file_out = ''
    i = -1
    while string[i] != '/' and len(string) + i > 0:
        file_out = string[i] + file_out
        string = string[:-1]

    return file_out, string

# prompts user for override input
def override_input():
    try:
        o_inp = input("Type 'o' for overwrite or 'a' for append: ")
        if o_inp.lower() != 'o' and o_inp.lower() != 'a':
            raise Exception('Error')
        else:
            return o_inp
    except Exception:
        print("Error. Enter either 'o' or 'a'.")
        return override_input()
    
# wrapped timing code for reusability, returns a function's runtime
def time_function(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    elapsed = round(end-start, 6)
    return elapsed

# list of colors for points
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
