import pandas as pd
import xlswriter
import os.path
  
urut = 1
file = urut + "A"

file_exists = os.path.exists(file)
workbook = xlsxwriter.Workbook(file)
worksheet = workbook.add_worksheet()

if file_exists == True:
    file = (urut += 1) + "A"
    new = False
elif file_exists == False:
    new = True

text = input("input text ")

