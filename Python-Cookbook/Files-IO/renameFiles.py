# Rename the files in the directory
import os
def rename_files():
    # Get the file names from a folder
    file_list = os.listdir(r"C:\Users\HP\Desktop\Python\Files-IO\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"C:\Users\HP\Desktop\Python\Files-IO\prank")
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

def remove_prefix(directory_path, prefix):
    file_list = os.listdir(directory_path)
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(directory_path)
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + file_name.lstrip(prefix))
        os.rename(file_name, file_name.lstrip(prefix))
    os.chdir(saved_path)

remove_prefix(r"/Users/adithinagarjuna/Downloads/Videos", "videos_")