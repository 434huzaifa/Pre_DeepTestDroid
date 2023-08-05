import splitfolders
import os
import shutil
# input_folder='G:\Download\Compressed\SortData8-03-2023-20230313T000312Z-001\SortData8-03-2023'
input_folder='G:\Download\Compressed\SortData8-03-2023-20230313T000312Z-001\SortData8-03-2023'
output_folder='C:/Users/Corrupted/Desktop/OUTPUT'
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
    os.makedirs(output_folder)
    
splitfolders.ratio(input_folder,output=output_folder,seed=33,ratio=(.7,.2,.1))