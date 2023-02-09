# %%
import os
from pandas import *
import csv
import pandas as pd
import math
import numpy as np
from pyhtml2pdf import converter

# %%
if not os.path.exists('output'):
   os.makedirs('output')

if not os.path.exists('output/Pdfs'):
   os.makedirs('output/Pdfs')

# %%
f = open("index.html",'r') 
filedata = f.read()
f.close() 
#print(filedata)

# %%
C = "HCS"
Date = "10-01-2023"
Camp = "Sweater"

# %%
data = read_csv("output/gsheet.csv",index_col = [0])

# %%


# %%
for N,P,G,O,Q,A in zip(data.Name,data.Phone,data.Gmail,data.Order_n,data.Quantity,data.Amount):
    invoice = filedata
       
    
    Tamount = round(float(A),2)
    Amount = round((Tamount*100)/105,2)
    Gst = round((Tamount*5)/105,2)
    
    
    

    
    
    #replace lines
    
        
    invoice = invoice.replace("@Name", str(N))


        
    invoice = invoice.replace("@Phone",str(P))

        
    invoice = invoice.replace("@Gmail",str(G))
       
        
    invoice = invoice.replace("@Invoice",str(O))
        

    invoice = invoice.replace("@Quantity",str(Q))
        
        
    invoice = invoice.replace("@Code",str(C))    
    
    
    invoice = invoice.replace("%Camp",str(Camp))   
        
    
        
    invoice = invoice.replace("₹Amount",str(Amount))       
        
      
    invoice = invoice.replace("₹Gst",str(Gst))       
    
        
    invoice = invoice.replace("₹TAmount","₹"+str(Tamount)) 
        
        
    invoice = invoice.replace("%Date",str(Date)) 
    
        
        
        
    f = open("output.html",'w')
    f.write(invoice) 
    f.close()     
    
    path = os.path.abspath('Output.html')
    converter.convert(f'file:///{path}', 'output/Pdfs/'+N+'.pdf')
        
    invoice = ""


# %%


# %%



# %%


# %%


# %%


# %%


# %%



