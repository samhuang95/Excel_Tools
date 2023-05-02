import pandas as pd
import os

file_dir = 'file_path'
# New file with combined information.
new_filename = file_dir + '\\new_file_name.xlsx'
file_list = os.listdir(file_dir)
new_list = []

for file in file_list:
    file_path = os.path.join(file_dir,file)
    # print(file_path)
    
    # transfer to DataFrame
    dataframe = pd.read_excel(file_path, engine='openpyxl')
    # print(dataframe)
    
    # Add a new column and name it after the file.
    dataframe['data_time'] = ''
    dataframe['data_time'] = dataframe['data_time'].apply(lambda x: os.path.basename(file).split('.')[2].split('_')[0])
    print(dataframe)

    new_list.append(dataframe)
  
df = pd.concat(new_list)
df.to_excel(new_filename,index=False)
