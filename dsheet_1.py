# %%
from pandas import *
import csv
import pandas as pd

# check the folder exist or not
import os
if not os.path.exists('output'):
   os.makedirs('output')

# read csv
data = read_csv("output/gsheet.csv")

#make list of donor and items
names = data['Customer'].tolist()
items = data['Items sold'].tolist()

# add index as Sno
data.insert(1, 'sno', range(1, 1 + len(data)))

# %%
#loop to make duplicate names
list = []
for i in data['sno']:
    j=i-1
#     print(names[j], items[j])
    if items[j] == 1:
       # print(names[j], items[j])
        list.append(names[j])
        
    elif items[j] > 1:
       # print(names[j], items[j], "***")
        for _ in range(items[j]):
            list.append(names[j])
            


# %%
list.reverse()


# %%
#make dict with Duplicate names & items 
sno = []
for a in range(len(list)):
    sno.append(a+1)
dict = {'sno': sno, 'Names': list}

# %%

final_list = pd.DataFrame(dict)


# %%
final_list.to_csv('output/dsheet.csv',index=False)

# %%



