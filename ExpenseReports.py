"""
These functions serve the purpose of analysis and visualization of data from the expense tracking process. 
It contains a GUI which provides different visualization options.
This files is meant to be a compliment to ExpenseTracker.py and is not neccessary for its use as an expense tracker.
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from tkinter import *
import tkinter as tk

from ExpenseTracker import load_df

def update_filts(df=df):
    """Updates dataframe filters matching boolean arrays. 
    All variables are global as their updated value is used outside the function.
    This function defaults to updating the filters for the main dataframe but can be used for any derivative"""
    global fast_food,grocery,fun,bills,other_exp,pets,household,exp_types,exp_filters,all_exp
    global discover,debit,red_card,cash,other_pay,pay_types,pay_filters,rent,all_pay
    
    fast_food = df['Expense Type'] == 'Fast Food'
    grocery  = df['Expense Type'] == 'Grocery'
    fun = df['Expense Type'] == 'Fun'
    bills = df['Expense Type'] == 'Bills'
    other_exp  = df['Expense Type'] == 'Other'
    pets = df['Expense Type']=='Pets'
    household = df['Expense Type'] == 'Household Supplies'
    rent = df['Expense Type'] =='Rent'
    car = df['Expense Type'] == 'Car'
    all_exp = fast_food|grocery|fun|bills|other_exp|pets|household|rent|car
    exp_types = ['Fast Food','Grocery','Household Supplies','Pets','Fun','Bills','Other','Rent']
    exp_filters = {'Fast Food':fast_food,'Grocery':grocery,'Fun':fun,
               Rent':rent,'Other':other_exp,'Pets':pets,
              'Household Supplies':household,'All':all_exp}
    
    discover = df['Payment Type']=='Discover'
    debit = df['Payment Type'] =='Debit'
    red_card = df['Payment Type'] == 'Red Card'
    cash = df['Payment Type'] == 'Cash'
    other_pay = df['Payment Type'] == 'Other'
    pay_types = ['Discover','Debit','Red Card','Cash','Other']
    all_pay = discover|debit|red_card|cash|other_pay
    pay_filters = {'Discover':discover,'Debit':debit,'Red Card':red_card,
                   'Cash':cash,'Other':other_pay,'All':all_pay}

df= ExpenseTracker.load_df() #loads dataframe into file

def month_by_month():
    """Creates line plot of expenses per month. Can be filtered by either type of payment, expense or both"""
    exp = str(cat.get()) #gets value of expense filter from GUI
    payment = str(pay.get())# gets value of payment filter from GUI
    months = []
    amounts = []
    for month in range(1,13):
        df_month = df[df['Month']==month]            
        update_filts(df_month) #updates filters for monthly dataframe
        filt = exp_filters[exp]|pay_filters[payment] # combines boolean filters selecting only wanted values
        months.append(month)
        amounts.append(df_month[filt]['Amount'].sum()) # sums all values from 'Amount' column from filtered dataframe
    plt.plot(months,amounts)
    plt.title(('{} Expenses Using {} Payment Method').format(exp,payment))
    plt.xtitle('Month')
    plt.ytitle('Amount Spent')
    update_filts() #resets filters to values from main dataframe
    plt.show()

def pie(pay_exp,types,filters,month = (df['Month'].iloc[-1]),comapre = False):
    """Creates pie chart from filtered data for specific month, using most recent as default"""
    update_filts() #updates dataframe filter
    all_labels = df[pay_exp].unique().tolist() #Collects all values of either payments or expenses present in dataframe
    labels = []
    amounts = []
    for label in types: #iterates through all expense or payment types
        if label in all_labels: #updates labels and amounts with values if expense or payment type is in dataframe
            df[filters[label][df['Month']==month]]['Amount'].sum()
            labels.append(label)
            amounts.append(df[filters[label]]['Amount'].sum())
    if compare: #allows values to be used in other functions
        return labels, amounts
    else: #plots pie chart as default
        plt.pie(amounts,shadow = True,labels=labels, startangle=180, autopct='%1.1f%%')
        plt.show()
        
  def pie_compare():
    """Creates two pie charts using the pie function"""
    month1 = int(month_1.get())
    month2 = int(month_2.get())
    labels1,amounts1= pie('Expense Type',exp_types,exp_filters,month1,compare=True)
    labels2,amounts2= pie('Expense Type',exp_types,exp_filters,month2,compare=True)
    plt.subplot(1,2,1)
    plt.title(('Expenses for Month {}').format(month1))
    plt.pie(amounts1,shadow = True,labels=labels1, startangle=180, autopct='%1.1f%%')
    plt.subplot(1,2,2)
    plt.title(('Expenses for Month {}').format(month2))
    plt.pie(amounts2,shadow = True,labels=labels2, startangle=180, autopct='%1.1f%%')
    fig.text(0.5, 1, txt, ha='center',fontsize=20)
    plt.show()
    
def pie_exp():
    """Creates pie chart of monthly expenses by expense type"""
    pie('Expense Type',exp_types,exp_filters)

def pie_pay():
    """Creates pie chart of monthly expenses by pay type"""
    pie('Payment Type',pay_types,pay_filters) 

def report_wind:
  win = tk.Tk()
  color='PeachPuff2'

  options = tk.Canvas(win,width =600,height=600,bg=color)
  options.pack()

  compare_month_pie_label = tk.Label(win,text='Compare Two Month\'s Pie Charts',bg=color)
  compare_month_pie_label.config(font=('Verdana',15),bg=color)
  options.create_window(400,50,window=compare_month_pie_label)

  month_1_label = tk.Label(win,text = 'Month 1', bg = color)
  month_1_label.config(font=('Verdana',15),bg=color)
  options.create_window(75,100,window=month_1_label)

  month_1 = tk.Entry(win)
  options.create_window(200,100,window=month_1)

  month_2_label = tk.Label(win,text = 'Month 2', bg = color)
  month_2_label.config(font=('Verdana',15),bg=color)
  options.create_window(325,100,window=month_2_label)

  month_2 = tk.Entry(win)
  options.create_window(450,100,window=month_2)

  compare_month_but = tk.Button(win,text = 'Compare Months',height=2,width= 20,command=pie_compare)
  options.create_window(650,100,window=compare_month_but)

  month_by_month_label = tk.Label(win,text='Month By Month Expenses')
  month_by_month_label.config(font=('Verdana',15),bg=color)
  options.create_window(400,175,window=month_by_month_label)

  cat = StringVar(win)
  cat.set("Fast Food")

  cat_labels = tk.Label(win,text='Select Expense Catagory To View:')
  cat_labels.config(font=('Verdana',12),bg=color)
  options.create_window(150,250,window=cat_labels)

  select_cat = OptionMenu(win, cat, 'Fast Food','Grocery','Household Supplies','Pets','Fun','Car','Rent','Other','All')
  select_cat.config(font=('Verdana', 10),bg='gray88')
  options.create_window(400,250, window=select_cat)

  month_by_month_but=tk.Button(win,text = 'View',height=2,width= 20)
  options.create_window(650,250,window=month_by_month_but)

  cat = StringVar(win)
  cat.set("All")

  cat_labels = tk.Label(win,text='Select Expense Catagory:')
  cat_labels.config(font=('Verdana',12),bg=color)
  options.create_window(150,250,window=cat_labels)

  select_cat = OptionMenu(win, cat, 'Fast Food','Grocery','Household Supplies','Pets','Fun','Car','Rent','Other','All')
  select_cat.config(font=('Verdana', 10),bg='gray88')
  options.create_window(400,250, window=select_cat)

  pay_labels = tk.Label(win,text='Select Payment\nType:')
  pay_labels.config(font=('Verdana',12),bg=color)
  options.create_window(200,320,window=pay_labels)

  pay = StringVar(win)
  pay.set("All")

  select_pay = tk.OptionMenu(win, pay,"Discover", "Red Card", "Debit", "Cash", "Other",'All')
  select_pay.config(font=('Verdana', 10),bg='gray88')
  options.create_window(400,320,window=select_pay)

  month_by_month_but=tk.Button(win,text = 'View',height=3,width= 20)
  options.create_window(650,285,window=month_by_month_but)
  
  month_rep_label=tk.Label(win,text = 'Month To Date Reports')
  month_rep_label.config(font=('Verdana',15),bg=color)
  options.create_window(400,400,window=month_rep_label)
    
  exp_pie = tk.Button(win,text ='Expense Type\nPie Chart',height=3,width = 30,command=pie_exp)
  options.create_window(250,475,window=exp_pie)
    
  pay_pie = tk.Button(win,text ='Payment Type\nPie Chart',height=3,width = 30,command=pie_pay)
  options.create_window(550,475,window=pay_pie)
    
  month = df['Month'].iloc[-1]
    
  exp_tot = tk.Label(test,text =('Total Expenses this Month: ${}').format(df[df['Month']==month]['Amount'].sum().round(2)))
  exp_tot.config(font=('Verdana',12),bg=color)
  options.create_window(400,500,window=exp_tot)
    
  last_month = df['Month'].iloc[-1]-1
  if last_month ==0:
      last_month = 1
    
  exp_last=tk.Label(test,text =('Total Expenses Last Month: ${}').format(df[df['Month']==last_month]['Amount'].sum().round(2)))
  exp_last.config(font=('Verdana',12),bg=color)
  options.create_window(400,550,window=exp_last)
  
  win.mainloop()
