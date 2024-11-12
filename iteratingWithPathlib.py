from pathlib import Path

# List all files in the current directory
for file in Path('.').iterdir():
    if file.is_file():
        print("File:", file.name)