from glob import glob
import os

remove_list = ["sample_site.com - "] # list of texts you want to remove

files_list = glob("*.mp4") # collect all files that are mp4

for f in files_list:
  for r in remove_list:
    
    f_new_name = f # copy the original name
    if r in f_new_name:
      f_new_name.replace(r,"") # remove sample_site from your file
      
    os.rename(f, f_new_name) # rename the file with new name
