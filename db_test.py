# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3

con = sqlite3.connect('/home/greg/programming/GutX/data/usda_db.db')

filepath = '/home/greg/programming/GutX/data/sr28asc/FOOD_DES.txt'
columns = ['NBD_No',
           'FdGrp_Cd',
           'Long_Desc',
           'Shrt_Desc',
           'ComName',
           'ManufacName',
           'Survey',
           'Ref_desc',
           'Refuse',
           'ScName',
           'N_Factor',
           'Pro_Factor',
           'Fat_Factor',
           'CHO_Factor']

def get_lines(filepath):
  with open(filepath, 'rb') as f:
    lines = f.readlines()
  return lines

lines = get_lines(filepath)
  
# get rid of carraige returns
lines = [_[:-4] for _ in lines]

# split by caret
lines = [_.split(b'^') for _ in lines]

# assign data types
def clean_data_type(row_item):
  try:
    row_item = row_item.decode('ascii')
  except UnicodeDecodeError as e:
    return 'ERROR'
    
  if len(row_item) == 0:
    return None
  elif row_item[0] == '~' and row_item[-1] == '~':
    output = str(row_item.replace('~', ''))
  elif '.' in row_item:
    output = float(row_item)
  else:
    output = int(row_item)
  return output

new_lines = []
for row in lines:
  new_row = []
  for item in row:
    new_row.append(clean_data_type(item))
  new_lines.append(new_row)
      
df = pd.DataFrame(new_lines, columns = columns)

df.to_sql('FOOD_DESC', con)
