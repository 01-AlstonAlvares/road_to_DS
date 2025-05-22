#Use os to create a folder and list all files in it.

import os
from os import write

folder_name = 'test_folder'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder ' {folder_name}' created.")
else:
    print(f"Folder ' {folder_name}' already exists.")

for i in range(3):
    with open(os.path.join(folder_name, f"file{i+1}.txt"), "w") as f:
        f.write(f"This is file {i+1}")

print("Files in folder")
for file_name in os.listdir(folder_name):
    print(file_name)
    print(file_name)
