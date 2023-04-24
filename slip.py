# %%
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas as pd
import math


 

import numpy as np

import os
if not os.path.exists('output/images'):
   os.makedirs('output/images')

# function to make slips with dsheet
def slip(num,cus):
    img = Image.open('input/pic.jpeg')
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('input/font/KGBlankSpaceSketch.ttf', 50)
    myFont1 = ImageFont.truetype('input/font/arial.ttf', 45)
    nums = str(num)
    
    # to eliminate the empty names
    k = str(cus)
    if k == "nan":
        cus = "  "
    else:
        print()
    
    d1.text((400, 300),str(cus),(0,0,0),anchor="mm",font=myFont)
    d1.text((690, 50),"#"+nums,(0,0,0),font=myFont1,align='centre')
   # img.show()
    img.save("output/images/"+nums+".jpg")


# %%


df = pd.read_csv('output/dsheet.csv', index_col = [0])

#print(df) 

# %%
names = df["Names"].tolist()
nums = df.index.tolist()


# %%

    


# %%


# %%


# %%
for i,j in zip(names,nums):
    #print(i,j)
    #print(type(j))
    #print("\n")

    slip(j,i)

# %%


# %%



