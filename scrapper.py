import os, sys
from shutil import copyfile

cwd = os.getcwd()
my_file_list = []

# get list of files that exist under the record folder
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
                            my_file_list.append(f'./{day}/{hour}/{minuteFile}')
else:
    print('Old folder was located please remove the folder')
    print('[copies] and execute script again')

# copy each file into a new folder numbered from 1 to ...
if my_file_list:
    count= 0
    if not os.path.exists('../copies'):
        os.mkdir('../copies')
    for file in my_file_list:
        count+=1
        copyfile(file, f'../copies/{count}.mp4')
        os.system("cls" if os.name=='nt' else "clear")
        print('Script is copying...')
        print(f"Files completed: {count}/{len(my_file_list)}")
else:
    print('No files were located, no copys were made\nABORTING')


# make copies of each file and place in root directory
# each file should be numbered from 1.mp4 to sumNum.mp4


# leave previous files intact in case of corrpution
# prompt for zip then clean up
