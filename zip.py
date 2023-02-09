# %%
import os
from zipfile import ZipFile

# %%
entries = os.listdir('output/pdfs')
entries

# %%
suffix = ".pdf"
files = [x for x in entries if x.endswith(suffix)]

files

# %%
f = ZipFile('output/pdfs.zip', 'w')
for i in files:
    f.write('output/Pdfs/'+i)

f.close()

# %%



