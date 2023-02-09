# %%
from bs4 import BeautifulSoup
import re
import os
from pyhtml2pdf import converter
from pandas import *
import csv
import pandas as pd
import math
import numpy as np


import os


if not os.path.exists('output'):
   os.makedirs('output')

if not os.path.exists('output/Pdfs'):
   os.makedirs('output/Pdfs')


    
C = "HCS"
Date = "10-01-2023"
Camp = "Sweater"

# %%
data = read_csv("output/gsheet.csv",index_col = [0])
data 

# %%
# replace function not in use
def replace(before,after):
    target = soup.find_all(text=re.compile(before))
    for v in target:
        v.replace_with(v.replace(before,after))

# %%



# %%

   

# %%
for N,P,G,O,Q,A in zip(data.Name,data.Phone,data.Gmail,data.Order_n,data.Quantity,data.Amount):
    with open("index.html") as fp:
        soup1 = BeautifulSoup(fp, "html.parser")
        
    soup = soup1
    
    Tamount = round(float(A),2)
    Amount = round((Tamount*100)/105,2)
    Gst = round((Tamount*5)/105,2)
    
    
    

    
    
    #replace lines
    target = soup.find_all(text=re.compile("@Name"))
    for v in target:
        v.replace_with(v.replace("@Name",str(N)))

    target = soup.find_all(text=re.compile("@Phone"))
    for v in target:
        v.replace_with(v.replace("@Phone",str(P)))

    target = soup.find_all(text=re.compile("@Gmail"))
    for v in target:
        v.replace_with(v.replace("@Gmail",str(G)))
        
    target = soup.find_all(text=re.compile("@Invoice"))
    for v in target:
        v.replace_with(v.replace("@Invoice",str(O)))
        
    target = soup.find_all(text=re.compile("@Quantity"))
    for v in target:
        v.replace_with(v.replace("@Quantity",str(Q)))
        
    target = soup.find_all(text=re.compile("@Code"))
    for v in target:
        v.replace_with(v.replace("@Code",str(C)))
        
    target = soup.find_all(text=re.compile("%Camp"))
    for v in target:
        v.replace_with(v.replace("%Camp",str(Camp)))
        
        
    target = soup.find_all(text=re.compile("₹Amount"))
    for v in target:
        v.replace_with(v.replace("₹Amount",str(Amount)))
        
    target = soup.find_all(text=re.compile("₹Gst"))
    for v in target:
        v.replace_with(v.replace("₹Gst",str(Gst)))
        
    target = soup.find_all(text=re.compile("₹TAmount"))
    for v in target:
        v.replace_with(v.replace("₹TAmount","₹"+str(Tamount)))  
        
        
        
    target = soup.find_all(text=re.compile("%Date"))
    for v in target:
        v.replace_with(v.replace("%Date",str(Date))) 
    
        
    s = str(soup)
    text_file = open("Output.html", "w")
    text_file.write(s)

    text_file.close()
    
    
    path = os.path.abspath('Output.html')
    converter.convert(f'file:///{path}', 'output/Pdfs/'+N+'.pdf')
        
    soup = ""



# %%



