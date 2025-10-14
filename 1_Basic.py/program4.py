# Write a python program to print the content of a Specific directory using the os module .

import os
directory_path ='c:/'

# List all entries in the specific directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
