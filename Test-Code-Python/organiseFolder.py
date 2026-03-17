# Write a python code to organise the folder by moving all the files of a particular type to a new folder named after that type.
# Sort Everything in this folder by file type. Rename files with clear descriptive names depending on the content of the file.
# If content is unknown, give it a generic but understandable name based on the existing file. Put documents in one subfolder, 
# images in another, spreadsheets in another, and so on.
# Put duplicates in another folder named "Duplicates", which I can verify and delete later.

import os
import shutil
import hashlib
from pathlib import Path

def get_file_type(file_path):
    # Determine the file type based on the extension
    file_extension = file_path.suffix.lower()
    if file_extension in ['.txt', '.pdf', '.doc', '.docx']:
        return 'Documents'
    elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
        return 'Images'
    elif file_extension in ['.xls', '.xlsx', '.csv']:
        return 'Spreadsheets'
    elif file_extension in ['.mp3', '.wav', '.flac']:
        return 'Audio'
    elif file_extension in ['.mp4', '.avi', '.mkv', '.mov']:
        return 'Videos'
    else:
        return 'Other'

def get_file_hash(file_path):
    # Generate a hash for the file to check for duplicates
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def organize_folder(folder_path):
    # Create a dictionary to store file hashes and paths
    file_hashes = {}
    duplicates_folder = Path(folder_path) / 'Duplicates'
    duplicates_folder.mkdir(exist_ok=True)

    # Initialize counters
    moved_files = 0
    renamed_files = 0
    duplicate_files = 0

    # Iterate over all files in the folder
    for file_path in Path(folder_path).iterdir():
        if file_path.is_file():
            # Get the file type and create the corresponding folder if it doesn't exist
            file_type = get_file_type(file_path)
            type_folder = Path(folder_path) / file_type
            type_folder.mkdir(exist_ok=True)

            # Generate a hash for the file
            file_hash = get_file_hash(file_path)

            # Check for duplicates
            if file_hash in file_hashes:
                # Move the duplicate file to the Duplicates folder
                duplicate_file_path = duplicates_folder / file_path.name
                shutil.move(str(file_path), str(duplicate_file_path))
                duplicate_files += 1
                print(f"Moved duplicate file: {file_path.name} to Duplicates folder")
            else:
                # Add the file hash to the dictionary
                file_hashes[file_hash] = file_path

                # Rename the file with a clear descriptive name
                new_file_name = f"{file_type.lower()}_{file_path.stem}{file_path.suffix}"
                new_file_path = type_folder / new_file_name

                # Move the file to the corresponding folder
                shutil.move(str(file_path), str(new_file_path))
                moved_files += 1
                renamed_files += 1
                print(f"Moved and renamed file: {file_path.name} to {new_file_name}")

    # Print the summary
    print_summary(moved_files, renamed_files, duplicate_files)

def print_summary(moved_files, renamed_files, duplicate_files):
    print("\nSummary of Actions Taken:")
    print(f"- Moved {moved_files} files to their respective folders.")
    print(f"- Renamed {renamed_files} files with clear descriptive names.")
    print(f"- Moved {duplicate_files} duplicate files to the Duplicates folder for verification and potential deletion.")

# Example usage
folder_path = '/Users/adithinagarjuna/Downloads'  # Change this to your target folder path
organize_folder(folder_path)