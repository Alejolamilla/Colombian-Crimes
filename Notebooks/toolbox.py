# This file contains useful functions used in the notebooks

import os
import pandas as pd

''' 
data_source = the forlder where the XLSX are hosted (str)
xlsx_list = a list with the xlsx files that whant to convert into dataframes (list)
avoid = the elements in the data_source that wants to avoid (list)
skip_rows = How many rows will be skeped on the XLSX (int)
skip_footer = rows that will avoid at the end of the document (int)
'''
def load_xlsx_dataframes(data_source = ".", xlsx_list = [], avoid = [], skip_rows = 0, skip_footer = 0):

    dataframes = {}
    
    if xlsx_list == []:
        # use os.listdir to get all the files and delete the elements listed on "avoid"
        xlsx_list = list(set(os.listdir(data_source)) - set(avoid))
    
    else:
        # delete the elements listed on "avoid" from the elements listed on "xls_list"
        xlsx_list = list(set(xlsx_list) - set(avoid))

    for file in xlsx_list:
        df = pd.read_excel(data_source + "/" + file, skiprows= skip_rows, skipfooter=skip_footer)
        df["DELITO"] = file

        dataframes[file] = df

    return dataframes


"""
dataframes = list with the dataframes that will be processed (list)
old_column_position = which is the index of the columns to update (int)
new_name = the new name that will have the columns
"""
def update_columns_name(dataframes, old_column_position, new_name):
    
    new_df_list = []

    for dataframe in dataframes:
        dataframe = dataframe.rename(columns = {dataframe.columns[old_column_position] : new_name})

        new_df_list.append(dataframe)

    return new_df_list
