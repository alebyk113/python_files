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


folder_list = [ '160614', '160615', '160616', '160620', '160621', '160622', '160628', '160630', '160720', '160721', '160722', '160725', '160727', '160728', '160729', '160801', '160803', '160804', '160808', '160810', '160811', '160812', '160815', '160816', '160819', '160822', '160824', '160825', '160902', '160905', '160922', '160923', '160926', '160927', '160928', '160929', '161002', '161004', '161005', '161006', '161007', '161017', '161020', '161025', '161026', '161028', '161101', '161107', '161108', '161109', '161110', '161111', '161114', '161116', '161117', '161121', '161122', '161123', '161124', '161125', '161128', '161130', '161201', '161204', '161208', '161209']

for folder_name in folder_list:    
    os.chdir("C:\\to_analyse")
    file_list=[]
    os.chdir(folder_name)
    
    for file in glob.glob("*.T1"):
        file_list.append(file)
    
    print(file_list)
    

        
    convert(file_list)