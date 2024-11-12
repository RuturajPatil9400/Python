import os

# List all files in a directory
for filename in os.listdir('.'):
    if os.path.isfile(filename):
        print("File:", filename)