import os
#import glob

#print glob.glob("/desktop/*.docx")

def convert(file_list):
    file_list=file_list
    for i in file_list:
        base = os.path.splitext(i)[0]
        os.rename(i, base + ".csv")
        print (i)
    
file_list=["63290355.AT0","63290348.AT0","63290341.AT0"] #,"65190095.AP0"]#,"63300548.AP0"]#,"63080109.AP0","63080119.AP0","63080144.AP0","63080156.AP0"]
#,"65310052.AP0","65310054.AP0","65310056.AP0","6531058.AP0","63080156.AP0","63080076.AP0",]
convert(file_list)