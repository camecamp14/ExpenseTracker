import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from ExpenseReport import *
def load_df():
    expense_file ="C:\\fakepath\\Expense.csv" #csv file to which all data is saved
    df = pd.read_csv(expense_file) #loads data into a dataframe for analysis and manipulation

load_df()
    
def enter():
    """Takes input values from GUI and updates dataframe and csv file"""
    global df
    global pay_type
    global exp_type
    global amount
    global date
    global memo
    pay_type = str(payment.get())
    exp_type = str(expense.get())
    amnt = float(amount.get())
    day = str(date.get())
    month = str(month_ent.get())
    memo = str(memo_ent.get())
    df = df.append({'Payment Type':pay_type,
                    'Expense Type':exp_type,
                    'Amount':amnt,
                    'Month':month,
                    'Day':day,
                   'Memo':memo},ignore_index=True
                  )
    df.to_csv(expense_file,index=False) #rewrites and updates csv file with updated info
    
    def update_filts():
    """Updates dataframe filters after new value is added. 
    Creates filters that classify data by either expense type, payment type, or month of purchase"""
    global fast_food,grocery,fun,kayla,bills,other_exp,pets,household,exp_types,exp_filters
    global discover,debit,red_card,cash,other_pay,pay_types,pay_filters
    global jan,feb,march,april,may,june,july,aug,sept,octo,nov,dec,all_month,month_filters
    
    jan = df['Month']==1
    feb = df['Month']==2
    march = df['Month']==3
    april = df['Month']==4
    may = df['Month']==5
    june = df['Month']==6
    july = df['Month']==7
    aug = df['Month']==8
    sept = df['Month']==9
    octo = df['Month']==10
    nov = df['Month']==11
    dec = df['Month']==12
    all_months = jan,feb,march,april,may,june,july,aug,sept,octo,nov,dec
    month_filters={'Jan':jan,'Feb':feb,'March':march,'April':april,'May':may,'June':june,
                  'July':july,'Aug':aug,'Sep':sept,'Oct':octo,'Nov':nov,'Dec':dec}
    
    fast_food = df['Expense Type'] == 'Fast Food'
    grocery  = df['Expense Type'] == 'Grocery'
    fun = df['Expense Type'] == 'Fun'
    kayla  = df['Expense Type'] == 'Kayla'
    bills = df['Expense Type'] == 'Bills'
    other_exp  = df['Expense Type'] == 'Other'
    pets = df['Expense Type']=='Pets'
    household = df['Expense Type'] == 'Household Supplies'
    rent = df['Expense Type'] =='Rent'
    car = df['Expense Type'] == 'Car'
    exp_types = ['Fast Food','Grocery','Household Supplies','Pets','Fun','Kayla','Bills','Other']
    exp_filters = {'Fast Food':fast_food,'Grocery':grocery,'Fun':fun,
               'Kayla':kayla,'Rent':rent,'Other':other_exp,'Pets':pets,
              'Household Supplies':household}
    
    discover = df['Payment Type']=='Discover'
    debit = df['Payment Type'] =='Debit'
    red_card = df['Payment Type'] == 'Red Card'
    cash = df['Payment Type'] == 'Cash'
    other_pay = df['Payment Type'] == 'Other'
    pay_types = ['Discover','Debit','Red Card','Cash','Other']
    pay_filters = {'Discover':discover,'Debit':debit,'Red Card':red_card,
                   'Cash':cash,'Other':other_pay}
    

def plots_tot():
    """Creats Pie Charts for total expenses by payment type and expense type"""
    update_filts()
    payments = df['Payment Type'].unique().tolist()
    payment_type = []
    payment_amount = []
    for pay in pay_types:
        if pay in payments:
            payment_type.append(pay)
            payment_amount.append(df[pay_filters[pay]]['Amount'].sum())
    expenses = df['Expense Type'].unique().tolist()
    exp_type = []
    exp_amount = []
    for exp in exp_types:
        if exp in expenses:
            exp_type.append(exp)
            df[exp_filters[exp]]['Amount'].sum()
            exp_amount.append(df[exp_filters[exp]]['Amount'].sum())
    txt=('Total Expenses: ${}').format(df['Amount'].sum().round(2))
    fig=plt.figure()
    plt.subplot(1,2,1)
    plt.pie(payment_amount,shadow = True,labels=payment_type, startangle=180, autopct='%1.1f%%')
    plt.subplot(1,2,2)
    plt.pie(exp_amount,shadow = True,labels=exp_type, startangle=180, autopct='%1.1f%%')
    fig.text(0.5, 1, txt, ha='center',fontsize=20)
    plt.show()
    fig.savefig("C:\\Users\\cam14\\Scripts\\Plots.png") 

root = tk.Tk()

color='PeachPuff2'

main = tk.Canvas(root, width = 600, height = 600,bg=color)
main.pack()

label1 = tk.Label(root, text='Expense Tracker')
label1.config(font=('Verdana', 25),bg=color)
main.create_window(300,30, window=label1)

payment = StringVar(root)
payment.set("Discover") # initial value

pay_label = tk.Label(root, text = 'Payment Type:')
pay_label.config(font=('Verdana',15),bg=color)
main.create_window(200,100, window=pay_label)

pay_opt = OptionMenu(root, payment, "Discover", "Red Card", "Debit", "Cash", "Other")
pay_opt.config(font=('Verdana', 10),bg='gray88')
main.create_window(400,100, window=pay_opt)

expense = StringVar(root)
expense.set("Fast Food")

exp_label = tk.Label(root, text = 'Expense Type:')
exp_label.config(font=('Verdana',15),bg=color)
main.create_window(200,175, window=exp_label)

exp_opt = OptionMenu(root, expense, 'Fast Food','Grocery','Household Supplies','Pets','Fun','Kayla','Car','Rent','Other')
exp_opt.config(font=('Verdana', 10),bg='gray88')
main.create_window(400,175, window=exp_opt)

memo_label = tk.Label(root, text='Memo:')
memo_label.config(font=('Verdana',15),bg=color)
main.create_window(200,250, window=memo_label)

memo_ent = tk.Entry(root)
main.create_window(400,250,window=memo_ent)

amount_label = tk.Label(root, text = 'Amount:')
amount_label.config(font=('Verdana',15),bg=color)
main.create_window(200,325, window=amount_label)

amount = tk.Entry(root)
main.create_window(400,325, window=amount)

month_label = tk.Label(root, text = 'Month:')
month_label.config(font=('Verdana',15),bg=color)
main.create_window(150,400, window=month_label)

month_ent = tk.Entry(root)
main.create_window(250,400,window=month_ent)

date_label = tk.Label(root, text ='Date:')
date_label.config(font=('Verdana',15),bg=color)
main.create_window(350,400, window=date_label)

date = tk.Entry(root)
main.create_window(450,400,window=date)


ent_but = tk.Button(root,text='Enter', height=3,width= 30, command=enter)
main.create_window(300,500,window=ent_but)

new_wind = tk.Button(root,text='Run Reports', height=3,width=30, command = ExpenseReport.report_wind)
main.create_window(300,560, window=new_wind)


root.mainloop()
