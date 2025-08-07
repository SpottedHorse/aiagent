import sys
from os import path, listdir

def get_files_info(working_directory, directory="."):
    path.join(working_directory, directory)
    
    
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    if directory not in working_directory:
        pass