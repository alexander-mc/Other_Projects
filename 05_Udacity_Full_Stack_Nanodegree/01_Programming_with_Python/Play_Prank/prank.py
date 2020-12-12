# Project name: Play Prank
# Course: Udacity Full Stack Nanodegree

# -----------------------------------

import os

def rename_files():
    path_name = "/Users/Alexander/Documents/Coding/Udacity/Full Stack Developer/1_Programming with Python/Documents/Lesson 2/prank"
    file_list = os.listdir(path_name)
    print file_list

    saved_path = os.getcwd()

    os.chdir(path_name)
    for old_file_name in file_list:
        new_file_name = old_file_name.translate(None, "0123456789")        
        print ("Old Name - "+old_file_name)
        print ("New Name - "+new_file_name)
        os.rename(old_file_name, new_file_name)

    print ("Operation Completed!")
    os.chdir(saved_path)
     
rename_files()
