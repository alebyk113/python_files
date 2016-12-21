import os
import glob


                  
#os.chdir("O:\python_files\rotation_data\csv_june_10")
def convert(file_list):
    file_list=file_list
    for i in file_list:
        base = os.path.splitext(i)[0]
        os.rename(i, base + ".csv")
        print (i)


#161006C
#161003
folder_list = [ "160309"]

for folder_name in folder_list:    
    file_list=[]
    os.chdir(folder_name)
    
    for file in glob.glob("*.P0"):
        file_list.append(file)
    
    print(file_list)
    

        
    convert(file_list)