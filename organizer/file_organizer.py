import os
import shutil

# Function to organize files based on file types (extensions)
def organize_files_by_extension(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    # Dictionary to map file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.tar', '.rar', '.gz'],
        'Code': ['.py', '.html', '.css', '.js', '.cpp', '.java'],
        'Others': []  # For files that do not match any known extensions
    }

    # Create subfolders if they don't already exist
    for folder in file_types:
        folder_path_sub = os.path.join(folder_path, folder)
        if not os.path.exists(folder_path_sub):
            os.makedirs(folder_path_sub)

    # Loop through the files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Determine the folder to move the file to based on its extension
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                # Move the file to the appropriate folder
                destination_folder = os.path.join(folder_path, folder)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {folder} folder.")
                moved = True
                break
        
        # If the file doesn't match any known extension, move it to 'Others'
        if not moved:
            destination_folder = os.path.join(folder_path, 'Others')
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to Others folder.")

# Specify the folder path you want to organize
folder_path = r'C:\Users\lavys\Downloads'

# Call the function to organize the files
organize_files_by_extension(folder_path)
