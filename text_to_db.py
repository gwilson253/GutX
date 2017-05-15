# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3


def get_lines(filepath):
  '''Read filepath as lines and return list.'''
  
  with open(filepath, 'rb') as f:
    lines = f.readlines()
  return lines


def clean_data_type(row_item):
  '''Takes a USDA datapoint, convert to ascii, and return typed equivalent.'''
  
  try:
    row_item = row_item.decode('ascii')
  except UnicodeDecodeError as e:
    return 'ERROR'
    
  if len(row_item) == 0:
    return None
  elif row_item[0] == '~' and row_item[-1] == '~':
    output = str(row_item.replace('~', ''))
  elif len(row_item) == 7 and row_item[2] == '/':
    output = str(row_item)
  elif '.' in row_item:
    output = float(row_item)
  else:
    output = int(row_item)
  return output


def file_to_sqlite(text_file_path, column_names, dest_table_name):
  '''Writes text file to sqlite table.'''
  
  con = sqlite3.connect('/home/greg/programming/GutX/data/usda_db.db')
  lines = get_lines(text_file_path)
  lines = [_[:-2] for _ in lines]
  lines = [_.split(b'^') for _ in lines]
  
  new_lines = []
  for row in lines:
    new_row = []
    for item in row:
      new_row.append(clean_data_type(item))
    new_lines.append(new_row)
        
  df = pd.DataFrame(new_lines, columns = column_names)
  df.to_sql(dest_table_name, con)
  