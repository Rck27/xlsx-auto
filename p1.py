import xlsxwriter
import pandas as pd
from pathlib import Path
import os.path
import openpyxl
import xlrd

file = 'tes.xlsx'
file_exists = os.path.exists(file)
if file_exists == False:
	workbook = xlsxwriter.Workbook(file)
	worksheet = workbook.add_worksheet()
	column = 0
	new = True
elif file_exists == True:
	df = pd.read_excel(file)
	nmpy= df.to_numpy()
	column = 1
	new = False

wholeString = input("input the whole text ")
#wholeString= "a 1 b 2 c 3 d 4"


#if wholeString.find(" ") == true :
newStr = wholeString.split(" ")

newlen = len(newStr)
lastlen = len(nmpy)
totlen = lastlen + newlen
z = 0
for x in newStr:
	temp = x
	if temp.isalpha() == True:
		if new == True:
			worksheet.write(column, 0, x)
		elif new == False:
			for c in nmpy:
				worksheet.write(column, 0, c)
			for d in newStr:
				worksheet.write(column, 0, d)

		
	elif temp.isnumeric() == True:
		if new == True:
			worksheet.write(column, 1, x)
			column += 1
		elif new == False:
			for c in nmpy:
				worksheet.write(column, 1, c)
			for d in newStr:
				worksheet.write(column, 1, d)
			column +=1

#print(df[1])



workbook.close()