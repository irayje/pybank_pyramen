#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pathing libraries
from pathlib import Path
import csv


# In[2]:


#set file path for data
menu_filepath = Path("Resources/menu_data.csv")
sales_filepath = Path("Resources/sales_data.csv")


# In[3]:


#set list to store csv
menu = []
sales = []


# In[5]:


#read menu file and add menu to empty menu list
with open(menu_filepath, 'r') as csvfile:
    menureader = csv.reader(csvfile, delimiter=',')
    header = next(menureader)
    for item in menureader:
        menu.append(item)


# In[6]:


#read sales file and add to empty sales list
with open(sales_filepath, 'r') as csvfile:
    salesreader = csv.reader(csvfile, delimiter=',')
    header = next(salesreader)
    for reciept in salesreader:
        sales.append(reciept)


# In[7]:


#create empty report dictionary
report = {}


# In[8]:


#check sales data
print(sales[0:7])


# In[9]:


#set empty menu items to store list of unique menu items
Menu_Item = []


# In[10]:


#for loop for menu items in sales and add to empty menu list with unique items
for items in sales:
    if items[::][4] not in Menu_Item: 
            Menu_Item.append(items[::][4])


# In[11]:


#check unique items
print(Menu_Item[0:20])


# In[13]:


#set dictionary for sales of dish
dish_sales = {}


# In[21]:


#Attempt one, checked unique dish in unique menu and tried to create a dictionary with zero
for dish in Menu_Item:
    if dish == sales[::][4]:
        dish_sales = dish_sales.update({dish:0})


# In[22]:


print(dish_sales)


# In[29]:


#Attempt two, tried to run each individual dish to get it to add the quantity to the dictionary but did not work
for dish in Menu_Item:
    if dish[0] == sales[::][4]:
         dish_sales = dish_sales.update({dish[0]:+ sales[::][3]})


# In[30]:


#got nothing in return 
print(dish_sales)


# In[20]:


#this the part where I got stuck and cannot figure out the script to write the rest since the above returns 'none'
#the next steps and goals would have been
#figure out how to nest a dictionary into a list into a dictionary into a list



