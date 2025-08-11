from os import path, listdir
from config import *


def get_file_content(working_directory, file_path):
  abs_working_dir = path.abspath(working_directory)
  target_path = path.abspath(path.join(working_directory, file_path))
  
  if not target_path.startswith(abs_working_dir):
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  
  if not path.isfile(file_path):
     return f'Error: File not found or is not a regular file: "{file_path}"'
  
  try:  
    with open(file_path, "r") as f:
      file_content_string = f.read(MAX_CHARS)