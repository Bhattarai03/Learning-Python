# Write a python program to print the content of a current directory using the os module .

import os

# List all entries in the current directory
entries = os.listdir()

# Print each entry
for entry in entries:
    print(entry)
