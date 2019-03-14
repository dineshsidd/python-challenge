# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:08:04 2019

@author: dsiddine
"""
import csv
votes = 0 
can_votes = 0
name = ''
candidates = []
candidate = {}
result = []
with open("Resources\election_data.csv") as file :
    df = csv.reader(file)
    next(df)
    df_sort = sorted(df, key=lambda row:row[2])

total_votes = len(df_sort)

for row in df_sort:
    votes = votes +1
    can_votes = can_votes + 1
    if (votes == 1 ):
        name = row[2]
    elif (name != row[2]) or (votes == total_votes) :
        if (votes != total_votes):
            can_votes = can_votes-1
            
        candidate.update({"name" : name})
        candidate.update({"votes" : can_votes})
        candidate.update({"Percent" : round(((can_votes)/total_votes) * 100,2)})
        candidates.append(candidate)  
        candidate = {}
        #print (name + ' : ' + str(can_votes))
        name = row[2]
        can_votes = 1

result.append("Election Results ")        
result.append("----------------------------")    
result.append("Total Votes : " + str(total_votes))
result.append("----------------------------")  


candidates_sorted = sorted(candidates, key=lambda row:row['votes'], reverse=True)
for row in candidates_sorted:
    result.append(row["name"] + "  :  " + str(row["Percent"]) + "% (" + str(row["votes"]) + ")")

result.append("----------------------------")
result.append(" Winner :" + candidates_sorted[0]["name"] )
result.append("----------------------------")

with open("polls_result.txt", 'w',newline = '') as file_w:
    for x in result: 
        file_w.writelines(x+"\n")
        print(x)
