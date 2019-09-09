#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pathlib and csv functions
import pandas as pd
from pathlib import Path
import csv


# In[2]:


#set the path
csvpath = Path("Resources/budget_data.csv")


# In[3]:


#set dataframe to variable
revenue_df = pd.read_csv(csvpath)


# In[4]:


#Find out total number of rows / months recorded
month_total = revenue_df.shape[0]


# In[5]:


#find total revenue
revenue_total = revenue_df['Profit/Losses'].sum()


# In[6]:


#add new column with changes month over month
revenue_changes = revenue_df['Change'] = revenue_df['Profit/Losses'].diff()


# In[7]:


#find average change
average_revenue_change = round(revenue_df['Change'].mean(),2)


# In[8]:


#find greatest incease in Change Column 
greatest_increase = round(revenue_df['Change'].max() , 2)


# In[9]:


#find greatest decrease in Change Column
greatest_decrease = round(revenue_df['Change'].min() , 2)


# In[10]:


greatest_decrease_data = revenue_df.loc[revenue_df['Change'] == greatest_decrease]


# In[11]:


#locate greastest increase data
greatest_increase_data = revenue_df.loc[revenue_df['Change'] == greatest_increase]


# In[12]:


#find greatest increase date 
greatest_increase_date = greatest_increase_data.iloc[0]['Date']


# In[13]:


#find greatest decrease date
greatest_decrease_date = greatest_decrease_data.iloc[0]['Date']


# In[14]:


# Set the output file path
output_path = Path('output.txt')

#create list to write 
output_text = ['Financial Analysis',
               '-' * 45,
               'Total Months: ' + str(month_total),
               'Average Change: $' + str(average_revenue_change),
               'Greatest Increase in Profits: ' + str(greatest_increase_date) + "($" + str(greatest_increase) +")",
               'Greatest Decrease in Profits: ' + str(greatest_decrease_date) + "($" + str(greatest_decrease) +")"
              ]

# Open the output path as a file object and write to file. 
with open("output.txt", "w") as text_file:
    for lines in output_text:
        print(lines, file=text_file)


# In[ ]:




