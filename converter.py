import os
import glob
import csv

#with open('folder_listv2.csv', 'r') as f:
#  reader = csv.reader(f)
#  your_list = list(reader)
#
#print(your_list)
                  
def convert(file_list):
    file_list=file_list
    for i in file_list:
        base = os.path.splitext(i)[0]
        os.rename(i, base + ".csv")
        print (i)


folder_list = [ 'sort']

for folder_name in folder_list:    
    os.chdir("C:\\python_files")
    file_list=[]
    os.chdir(folder_name)
    
    for file in glob.glob("*.xlsx"):
        file_list.append(file)
    
    print(file_list)
    

        
    convert(file_list)