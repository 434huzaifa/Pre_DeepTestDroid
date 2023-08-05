import os
import shutil
import csv
import splitfolders
import pyautogui
c_path = 'G:\\Download\\blackbox_dataset'
m_path = 'G:/Download/Compressed/rico_dataset_v0.1_semantic_annotations/semantic_annotations'
csv_path = "G:\OneDrive - MSFT\Huzaifa\CODE\TEEESSST\data2_all.csv"
loog = open('notfound.txt', 'w')
folder_list = ['very-low',
               'low',
               'medium',
               'high',
               'very-high']

class_range_start = [1, 7, 12, 19, 31]
class_range_end = [6, 11, 18, 30, 60]

LIMIT = -1  # -1 to do all


def copyfile(image_name, file_name):
    shutil.copy(os.path.join(m_path, image_name),
                os.path.join(c_path, file_name, image_name))


def fileChekerAndCreate(copy_path, file_name):
    full_path = os.path.join(copy_path, file_name)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        print('CREATED '+file_name)
# def ResetCopyFolder():
#     shutil.rmtree(c_path)
#     os.mkdir(c_path)


def sorterr():
    count = 0
    if len(class_range_start) == len(folder_list) == len(class_range_end):
        for i in folder_list:
            fileChekerAndCreate(c_path, i)
        if os.path.exists(csv_path):
            ccsv = csv.DictReader(open(csv_path, 'r'))
            for i in ccsv:
                image_name = i['name'].split('.')[0]+'.png'
                try:
                    component = int(i['component'])
                    for j in range(len(folder_list)):
                        if component >= class_range_start[j] and component <= class_range_end[j]:
                            copyfile(image_name, folder_list[j])
                            count += 1
                            print(count)

                            break
                    if count == LIMIT:
                        break
                except FileNotFoundError:
                    print('Cant Find '+image_name)
        else:
            print('Cant find CSV')
    else:
        print('maybe end or start or class name mising or added no idea length didnt match')
    print('FILE SORTED')


def spliter():
    input_folder = 'C:/Users/Corrupted/Desktop/SS2'
    output_folder = 'C:/Users/Corrupted/Desktop/OUTPUT'
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
        os.makedirs(output_folder)
    splitfolders.ratio(input_folder, output=output_folder,
                       seed=45, ratio=(.7, .2, .1))
    print('SPLITED')

def autoGUI():
    pyautogui.hotkey('ctrl','shift','a')
    pyautogui.press('backspace')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','shift','a')
    pyautogui.typewrite('run all')
    pyautogui.press('enter')
    


sorterr()
# spliter()
#autoGUI()
