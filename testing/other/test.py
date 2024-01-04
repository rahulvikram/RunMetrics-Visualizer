import tkinter as tk
from tkinter import filedialog
import sys
import csv

sys.path.append('src')
from module import Timer

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
        

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()