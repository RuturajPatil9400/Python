import os

# Get directory information like permissions
dir_info = os.stat('new_directory')
print(f"Directory permissions: {oct(dir_info.st_mode)}")