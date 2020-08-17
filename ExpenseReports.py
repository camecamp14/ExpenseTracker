import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from tkinter import *
import tkinter as tk

root = tk.Tk()
color='PeachPuff2'

options = tk.Canvas(root,width =600,height=600,bg=color)
options.pack()

compare_month_pie_label = tk.Label(root,text='Compare Two Month\'s Pie Charts',bg=color)
compare_month_pie_label.config(font=('Verdana',15),bg=color)
options.create_window(400,50,window=compare_month_pie_label)

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

month_by_month_label = tk.Label(root,text='Month By Month Expenses')
month_by_month_label.config(font=('Verdana',15),bg=color)
options.create_window(400,175,window=month_by_month_label)

cat = StringVar(root)
cat.set("Fast Food")

cat_labels = tk.Label(root,text='Select Expense Catagory To View:')
cat_labels.config(font=('Verdana',12),bg=color)
options.create_window(150,250,window=cat_labels)

select_cat = OptionMenu(root, cat, 'Fast Food','Grocery','Household Supplies','Pets','Fun','Kayla','Car','Rent','Other','All')
select_cat.config(font=('Verdana', 10),bg='gray88')
options.create_window(400,250, window=select_cat)

month_by_month_but=tk.Button(root,text = 'View',height=2,width= 20)
options.create_window(650,250,window=month_by_month_but)

cat = StringVar(root)
cat.set("All")

cat_labels = tk.Label(root,text='Select Expense Catagory:')
cat_labels.config(font=('Verdana',12),bg=color)
options.create_window(150,250,window=cat_labels)

select_cat = OptionMenu(root, cat, 'Fast Food','Grocery','Household Supplies','Pets','Fun','Kayla','Car','Rent','Other','All')
select_cat.config(font=('Verdana', 10),bg='gray88')
options.create_window(400,250, window=select_cat)

pay_labels = tk.Label(root,text='Select Payment\nType:')
pay_labels.config(font=('Verdana',12),bg=color)
options.create_window(200,320,window=pay_labels)

pay = StringVar(root)
pay.set("All")

select_pay = tk.OptionMenu(root, pay,"Discover", "Red Card", "Debit", "Cash", "Other",'All')
select_pay.config(font=('Verdana', 10),bg='gray88')
options.create_window(400,320,window=select_pay)

month_by_month_but=tk.Button(root,text = 'View',height=3,width= 20)
options.create_window(650,285,window=month_by_month_but)


root.mainloop()
