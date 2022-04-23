import pandas as pd
import pyexcel as pe
import numpy as np

file = 'tes.xlsx'
df = pd.read_excel('tes.xlsx')
aray = df.to_numpy()
df2 = pd.read_excel('t.xlsx')
aray2 = df2.to_numpy()

sumaray = np.append(aray, aray2)

mainaray = np.array(sumaray)
print("ar1 ", aray)
print("ar2 ", aray2)
print(sumaray[2])
print(sumaray[2].isalpha())
#print(aray2)