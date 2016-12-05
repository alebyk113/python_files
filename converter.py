import os
import glob

file_list=[]
                  
os.chdir("O:\python_files\dec_2_pyramidal")
for file in glob.glob("*.P0"):
     file_list.append(file)

print(file_list)

def convert(file_list):
    file_list=file_list
    for i in file_list:
        base = os.path.splitext(i)[0]
        os.rename(i, base + ".csv")
        print (i)
    
convert(file_list)