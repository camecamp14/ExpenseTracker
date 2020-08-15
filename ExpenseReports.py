import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from tkinter import *
import tkinter as tk

root = tk.Tk()
color='PeachPuff2'

options = tk.Canvas(root,width =600,height=600,bg=color)
options.pack()

month_1_label = tk.Label(root,text = 'Month 1', bg = color)
month_1_label.config(font=('Verdana',15),bg=color)
options.create_window(75,100,window=month_1_label)

month_1 = tk.Entry(root)
options.create_window(200,100,window=month_1)

month_2_label = tk.Label(root,text = 'Month 2', bg = color)
month_2_label.config(font=('Verdana',15),bg=color)
options.create_window(325,100,window=month_2_label)

month_2 = tk.Entry(root)
options.create_window(450,100,window=month_2)

compare_month_but = tk.Button(root,text = 'Compare Months',height=2,width= 20)
options.create_window(650,100,window=compare_month_but)

root.mainloop()
