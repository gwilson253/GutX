#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/greg/programming/GutX')
import text_to_db
import os

folder_path  = '/home/greg/programming/GutX/data/sr28asc'

# food descriptions table
filepath = os.path.join(folder_path, 'FOOD_DES.txt')
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
text_to_db.file_to_sqlite(filepath, columns, 'FOOD_DES')

# Food Group Description file
filepath = os.path.join(folder_path, 'FD_GROUP.txt')
columns = ['FdGrp_Cd', 'FdGrp_Desc']
text_to_db.file_to_sqlite(filepath, columns, 'FD_GRP')

# Langual Factor file
filepath = os.path.join(folder_path, 'LANGUAL.txt')
columns = ['NBD_No', 'Factor_Code']
text_to_db.file_to_sqlite(filepath, columns, 'LANGUAL')

# Langual Factors Description file
filepath = os.path.join(folder_path, 'LANGDESC.txt')
columns = ['Factor_Code', 'Description']
text_to_db.file_to_sqlite(filepath, columns, 'LANGDESC')

# Nutrient Data file
filepath = os.path.join(folder_path, 'NUT_DATA.txt')
columns = ['NBD_No',
           'Nutr_No',
           'Nutr_Val',
           'Num_Data_Pts',
           'Std_Error',
           'Src_Cd',
           'Deriv_Cd',
           'Ref_NDB_No',
           'Add_Nutr_Mark',
           'Num_Studies',
           'Min',
           'Max',
           'DF',
           'Low_EB',
           'Up_EB',
           'Start_cmt',
           'AddMod_Date',
           'CC']
text_to_db.file_to_sqlite(filepath, columns, 'NUT_DATA')

# Nutrient Definition Definition file
filepath = os.path.join(folder_path, 'NUTR_DEF.txt')
columns = ['Nutr_No',
           'Units',
           'Tagname',
           'NutrDesc',
           'Num_Desc',
           'SR_Order']
text_to_db.file_to_sqlite(filepath, columns, 'NUTR_DEF')

# Source Code File
filepath = os.path.join(folder_path, 'SRC_CD.txt')
columns = ['Src_Cd', 'SrcCd_Desc']
text_to_db.file_to_sqlite(filepath, columns, 'SRC_CD')

# Data Derivation Code Description
filepath = os.path.join(folder_path, 'DERIV_CD.txt')
columns = ['Deriv_Cd', 'Deriv_Desc']
text_to_db.file_to_sqlite(filepath, columns, 'DERIV_CD')

# Weight file
filepath = os.path.join(folder_path, 'WEIGHT.txt')
columns = ['NBD_No',
           'Seq',
           'Amount',
           'Msre_Desc',
           'Gm_Wgt',
           'Num_Data_Pts',
           'Std_Dev']
text_to_db.file_to_sqlite(filepath, columns, 'WEIGHT')

# Footnote File
filepath = os.path.join(folder_path, 'FOOTNOTE.txt')
columns = ['NBD_No',
           'Footnt_No',
           'Footnt_Typ',
           'Nutr_No',
           'Footnt_Txt']
text_to_db.file_to_sqlite(filepath, columns, 'FOOTNOTE')

# Sources of Data Link File
filepath = os.path.join(folder_path, 'DATSRCLN.txt')
columns = ['NBD_No', 'Nutr_No', 'DataSrc_ID']
text_to_db.file_to_sqlite(filepath, columns, 'DATSRCLN')

# Sources of Data File
filepath = os.path.join(folder_path, 'DATA_SRC.txt')
columns = ['DataSrc_ID',
           'Authors',
           'Title',
           'Year',
           'Journal',
           'Vol_City',
           'Issue_State',
           'Start_Page',
           'End_Page']
text_to_db.file_to_sqlite(filepath, columns, 'DATA_SRC')
