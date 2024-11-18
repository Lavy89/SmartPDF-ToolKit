# SmartPDF-ToolKit
SmartPDF ToolKit is a versatile and user-friendly PDF utility tool built using Python and Tkinter. It provides a range of features to perform operations on PDF files, making document management easier and more efficient.

## Features:
##### 1. Upload PDF:

  Select and load a PDF file into the application for further operations.

##### 2.Extract Text:

    Extract text from the entire PDF or a specific page.
    
    View the extracted text in a scrollable text area.
    
##### 3.Merge PDFs:

    Combine two PDF files into a single document.
    
    Save the merged PDF to a location of your choice.
    
##### 4.Split PDF:

    Split a PDF into two parts based on a specified page number.
    
    Save each part as a separate PDF file.
    
##### 5.Compress PDF:

    Reduce the size of a PDF without losing content quality.
    
##### 6.Convert PDF to Images:

    Convert all pages of a PDF into individual image files.
    
##### 7.Convert Images to PDF:

    Combine multiple image files into a single PDF document.
    
##### 8.Convert Text to PDF:

    Convert the contents of a text file into a PDF document.

    
## Prerequisites:

 Before running the application, ensure that you have the following libraries installed:
 
   tkinter (comes pre-installed with Python)
   
   PyPDF2
   
   pdf2image
   
   Pillow (PIL)
   
   reportlab
   

## How to Use:

  Run the program:

  Upload a PDF: Click on the Upload PDF button to select a file.

  Choose from the available operations:

  Extract text
  
  Merge PDFs
  
  Split PDF
  
  Compress PDF
  
  Convert PDF to images
  
  Convert images to PDF
  
  Convert text to PDF
  
## View Output:

  For operations involving text extraction, view the output in the scrollable text area.
  
  For other operations, save the output file to your desired location when prompted.









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

  

