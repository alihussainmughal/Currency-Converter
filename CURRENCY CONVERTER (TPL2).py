#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import requests

ENDPOINT = 'https://openexchangerates.org/api/latest.json'
APP_ID = '19b940401e8d43ae9c7c6416d202f063'
def convert():
  
    # Make a request to the latest exchange rates API endpoint
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={APP_ID}')

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the JSON response and extract the exchange rates data
        exchange_rates = response.json()['rates']  # is a dictionary that contains the exchange rates of different
        # currencies with respect to a base currency.
        print(exchange_rates)
        currency_1 = clicked.get()  # here we get the option from list 1
        currency_2 = clicked1.get()  # here i get the option from list 2
        amount = float(ent.get())  # here the value user will give
        rate_1 = exchange_rates[currency_1]
        rate_2 = exchange_rates[currency_2]
        converted_amount = round(amount / rate_1 * rate_2,2)  # The result is rounded to two decimal places using the round()
        formated = '{:,.2f}'.format(converted_amount)
        rlbl['text'] = formated
        print(converted_amount, formated)

    else:
        print(f'Request failed with status code {response.status_code}')

def reset():
    rlbl.config(text=' ')
    d1.current('0')
    d2.current('0')
    ent.delete(0,END)



root = tk.Tk()
root.geometry("350x300")
root.title("Currency Converter")
img=Image.open("C:/Users/tajummal\Downloads/a.jpg")
resize=img.resize((350,300),Image.ANTIALIAS)
nimg=ImageTk.PhotoImage(resize)

L=Label(image=nimg)
L.place(x=0,y=0,relwidth=1,relheight=1)
clicked  = tk.StringVar()
list=[ 'Currency_1','EUR', 'GBP', 'JPY',"ANG","PKR", "USD"]
name=tk.Label(text=" Ali Hussain   BCS203166",bg='lightgrey',fg='white',width=20)
name.grid(row=0,column=0)

lb=ttk.Label(text=" From") # our 1st label "from"
lb.grid(row=1,column=0,pady=5) # placing
d1=ttk.Combobox(root,textvariable=clicked,values=list) ## for dropdown menu Combobox is used with nessessry parameters
d1.current(0) # it show 1 elemnt of the menu
d1.grid(row=2,column=0,pady=5) #placing
clicked1=tk.StringVar() # declearing var with type


list1=['Currency_2 ','USD', 'EUR', 'GBP', 'JPY',"ANG","PKR"]# list 2 for second menu
lb1=ttk.Label(text="To") # second label
lb1.grid(pady=5,row=1,column=1) #placing
d2=ttk.Combobox(root, values=list1,textvariable=clicked1)# for menu
d2.current(0)
d2.grid(pady=5,row=2,column=1) #placing

lbl2=tk.Label(text="Enter Amount",bg='lightgrey')
lbl2.grid(pady=5,row=3,column=0)
ent=tk.Entry(width=25,bg='lightgrey')
ent.grid(pady=5,row=4,column=0)

b=tk.Button(text="Convert",command=convert,bg='lightgrey',width=22)# for tk.button with its paremeters
b.grid(pady=5,row=5,column=0)# placing

rlbl=tk.Label(text="Converted Amount ",bg="lightgrey")
rlbl.grid(pady=5,row=4,column=1)

b1=tk.Button(text=" Reset",command=reset,bg="lightgrey",width=20).grid(pady=5,row=5,column=1)

root.mainloop()


# In[ ]:





# In[ ]:




