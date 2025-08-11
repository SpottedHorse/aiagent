from os import path, listdir

def get_files_info(working_directory, directory="."):
    abs_working_dir = path.abspath(working_directory)
    target_dir = path.abspath(path.join(working_directory, directory))
    
    # If the absolute path to the directory is outside the working_directory, return a string error message:
    # if the abspath of 'directory' ends before the working directory return an error
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in listdir(target_dir):
            filepath = path.join(target_dir, filename)
            file_size = 0
            is_dir = path.isdir(filepath)
            file_size = path.getsize(filepath)
            files_info.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"