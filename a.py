import xlsxwriter
import pandas as pd
from pathlib import Path
import os.path
import openpyxl
import xlrd
import numpy as np

file = 't.xlsx'
file_exists = os.path.exists(file)
workbook = xlsxwriter.Workbook(file)
worksheet = workbook.add_worksheet()

if file_exists == False:
	column = 0
	new = True
elif file_exists == True:
	oldf = pd.read_excel(file)
	old= oldf.to_numpy()
	column = len(old)
	new = False
	print("file_exists, but thats fine")

mdf = pd.DataFrame(columns=['name', 'num'])

wholeString = input("input the whole text ")
#wholeString= "a 1 b 2 c 3 d 4"

newstr = wholeString.split(" ")
if new == False:
	aray = np.append(old, newstr)
else:
	aray = newstr

newsum = len(aray)

#print("file_exists, but thats fine")
for i in aray:
	temp = i
	if temp.isalpha() == True:
		worksheet.write(column, 0, i)
	if temp.isnumeric() == True:
		worksheet.write(column, 1, i)
		#worksheet.write(column, 1, i)
		column += 1
workbook.close()