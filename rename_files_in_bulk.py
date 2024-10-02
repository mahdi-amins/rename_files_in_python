from glob import glob
import os

remove_list = ["sample_site.com - "] 

files_list = glob("*.mp4")

for f in files_list:
  for r in remove_list:
    
    f_new_name = f
    if r in f_new_name:
      f_new_name.replace(r,"")
      
    os.rename(f, f_new_name)
