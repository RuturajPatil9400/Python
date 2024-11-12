from pathlib import Path

# Create a Path object for a directory
directory = Path('new_directory')

# Check if the directory exists
if directory.exists():
    print("Directory exists.")
else:
    print("Directory does not exist.")

# Create the directory 
directory.mkdir(parents=True, exist_ok=True)