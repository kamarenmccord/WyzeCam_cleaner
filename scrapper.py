import os
import sys
from shutil import copyfile


"""
    # a simple script that takes a series of files from a collection of organized folders and collects them all into one folder and numbers each of the files from  1.mp4 up to sumNum.mp4

    designed for wyze cam quick extraction of video files

    does not overwrite or erase old files incase of corruption or scripting error

"""

cwd = os.getcwd()
my_file_list = []

if sys.argv[1] and os.path.isdir(sys.argv[1]):
    my_file_list = os.listdir(f'./{sys.argv[1]}')

# get list of files that exist under the record folder
if not my_file_list:
    if not os.path.exists('./copies'):  # prevent overwrite
        if os.path.exists('./record'):
            os.chdir('./record')
            # get list of day folders
            for day in sorted(os.listdir('./')):
                if day.isnumeric():
                    for hour in sorted(os.listdir(f'./{day}')):
                        # get each hour folder under each day
                        for minuteFile in os.listdir(f'./{day}/{hour}'):
                            # get each minute file under each hour
                            if minuteFile:
                                my_file_list.append(
                                    f'./{day}/{hour}/{minuteFile}')
    else:
        print('Old folder was located please remove the folder')
        print('[copies] and execute script again')

# copy each file into a new folder numbered from 1 to ...
if my_file_list:
    count = 0
    if not os.path.exists('../copies'):
        os.mkdir('../copies')
    for file in my_file_list:
        count += 1
        copyfile(file, f'../copies/{count}.mp4')
        os.system("cls" if os.name == 'nt' else "clear")
        print('Script is copying...')
        print(f"Files completed: {count}/{len(my_file_list)}")
else:
    print('No files were located, no copys were made\nABORTING')
