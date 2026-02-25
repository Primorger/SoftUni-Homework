'''
..\SoftUni-Homework\Soft_Uni\Python_OOP_2026

'''
import os

lecture_name = input("Input the theme name: ")
files_path = input("Input the path for the files: ")
file_extention = input("Input the file extention: ")
files = []
digits = "0123456789"

def format_file_name(file_name):
    if file_name[0] in digits:
        final_file_name = file_name[4:].replace(" ", "_")
    else:
        final_file_name = file_name.replace(" ", "_")
    return final_file_name

def get_formated_file_names():
    while True:
        exersise_name = input("Input the file name: ")
        if exersise_name == "":
            break
        files.append(format_file_name(exersise_name) + file_extention)

def create_files(files_list):
    folder_path = os.path.join(files_path, format_file_name(lecture_name))
    
    os.makedirs(folder_path, exist_ok=True)

    for file in files_list:
        file_path = os.path.join(folder_path, file)
        while os.path.exists(file_path):
            print()
            new_name = input(f"File {file} already exists. Please enter a new name: ") + file_extention
            file_path = os.path.join(folder_path, new_name)
        
        with open(file_path, 'w') as f:
            pass

get_formated_file_names()
create_files(files)