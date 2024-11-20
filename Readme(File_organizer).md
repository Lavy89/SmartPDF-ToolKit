# File Organizer


This Python project helps you organize files in a specified folder based on their file types. The script scans the folder and sorts files into subfolders such as Images, Documents, Videos, Audio, Archives, Code, and Others. Files are moved according to their extensions.

## Features

Organize files by type: Files are moved into subfolders based on their extension.

Handles multiple file types: Categorizes files into types like Images, Documents, Videos, Audio, Code, etc.

Automatically creates subfolders: Subfolders are automatically created if they don’t exist.

Handles unknown file types: Files that don't match any specified type are moved to the "Others" folder.


## Requirements

Python 3.x

os and shutil modules (both are part of Python's standard library, so no installation is needed).


## How to Use

##### Clone this repository:

 ```git clone https://github.com/Lavy89/SmartPDF-ToolKit.git```


##### Navigate to the folder containing the script and the files you want to organize:

 ```cd /path/to/your/folder```


##### Run the script: Make sure to replace 'your_folder_path_here' with the path to the folder you want to organize:

 ```python file_organizer.py```


##### The script will organize the files based on their extensions:

Images: .jpg, .png, .gif, .bmp, .tiff

Documents: .pdf, .docx, .txt, .xlsx, .pptx

Videos: .mp4, .avi, .mov, .mkv

Audio: .mp3, .wav, .flac

Archives: .zip, .tar, .rar, .gz

Code: .py, .html, .css, .js, .cpp, .java

Others: Files that do not match any extension will be moved here.

  
