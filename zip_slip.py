# %%
import os
from zipfile import ZipFile

# %%
entries = os.listdir('output')
entries

# %%
suffix = ".docx"
files = [x for x in entries if x.endswith(suffix)]

files

# %%
f = ZipFile('output/doc.zip', 'w')
for i in files:
    f.write('output/'+i)

f.close()

# %%



