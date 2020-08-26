# ExpenseTracker
To be used, user must specify a csv file and include its path as the 'expense_path' variable prior to use. 
Columns must be: 'Payment Type, Expense Type, Amount, Month, Day, Memo'

Payment Type: Includes all possible types of payment for the user. 
  Examples: Cash, Credit Cards, Debit Cards, Autopayment ect.
  
Expense Type: Splits Expenses into categories.
  Examples: Rent, Utilites, Groceries, Gas, Fun ect.
  
Amount: Amount spend in desired currency. Do not include symbols such as $

Month: Two digit number representing the month of expense. 
  Example format: Janurary->01, November->11
  
Day: Two digit number representing the date

Memo (*Optional*): Allows user to annotate expense with details.
  Only visible on csv file (New feature to make visible may be added at a later time)
  
Program runs in ExpenseTracker.py which is the program that is responsible for providing a user interface and writing data to the csv file. ExpenseReport.py allows user to analyze and visual expenses. Clicking the 'Run Reports' button opens a new window which calls upon the ExpenseReport.py file. Within this file is the program for the new user interface to select graphs to display, as well as the functions required to filter, calculate, and plot data as requested.

Requirements:
Python3.7 or newer
numpy
Pandas
tkinter
matplotlib
