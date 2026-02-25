r'''
\SoftUni-Homework\Soft_Uni\Python_OOP_2026

'''
import os
import re

lecture_name = input("Input the theme name: ").strip()
files_path = input("Input the path for the files: ").strip()
file_extention = input("Input the file extention: ").strip()
files = []
digits = "0123456789"

def format_file_name(file_name):
    if not file_name:
        return ""
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
    raw = files_path.replace("\n", "").replace("\r", "")
    s = raw.strip()
    if not s:
        base_path = os.getcwd()
    else:
        s = os.path.expanduser(s)
        is_unc = s.startswith('\\\\')
        has_drive = re.match(r'^[A-Za-z]:[\\/]', s) is not None
        if is_unc or has_drive:
            base_path = os.path.abspath(s)
        elif s.startswith(('\\', '/')):
            rel = s.lstrip('\\/')
            base_path = os.path.abspath(os.path.join(os.getcwd(), rel))
        else:
            base_path = os.path.abspath(s)

    folder_path = os.path.join(base_path, format_file_name(lecture_name))
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