# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:01:53 2019

@author: Dinesh Siddineni
"""

import csv 
import os

total_months = 0 
total = 0 
mean = 0
increase = 0
greatest_increase  = 0
greatest_decrease  = 0
big_month  = ''
small_month = ''
result = []
path = os.path.join("Resources","budget_data.csv")

with open(path) as file :
    csv_reader = csv.reader(file,delimiter=",")
    next (csv_reader)
    #get_withsum = sum(x for x in csv_reader[0])
    #get_sum = (int(a[1]) for a in csv_reader)
    for row in csv_reader:
        total_months = total_months + 1 
        total = total  + int(row[1])
        if ( total_months == 1):
            low = int(row[1])
        if (total_months > 1) :
            high = int(row[1])
            increase = (high - low)
            mean = mean + increase
            low = high
        if increase > greatest_increase :
            big_month = row[0]
            greatest_increase = increase
        if increase < greatest_decrease :
            small_month = row[0]
            greatest_decrease = increase
    
    result.append("Financial Analysis")
    result.append("-----------------------------------------------")
    result.append("Total Months : " +  str(total_months))
    result.append("Total : $" +  str(total) )
    result.append("Average Change :$" + str(round(mean/(total_months-1),2)))
    result.append("Greatest Increase in Profits : $" + str(big_month) + " (" + str(greatest_increase) + ")") 
    result.append("Greatest Decrease in Profits : $" + str(small_month) + " (" +str(greatest_decrease) + ")" )
    
    
    
with open("budget_data_out.csv" ,'w', newline ='') as file_w:
    csv_writer = csv.writer(file_w, delimiter=",")
    for x in result:
        csv_writer.writerow([x])
        print(x)

    