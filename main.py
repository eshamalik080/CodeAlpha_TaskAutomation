import os
import shutil

source = r"C:\Users\MR LAPTOP\Desktop\uni\images"

destination = r"C:\Users\MR LAPTOP\Desktop\jpgFiles"

if not os.path.exists(destination):
    os.makedirs(destination)
    print("Destination folder is created")

for file_name in os.listdir(source):
    if  file_name.lower().endswith(".jpg"):
        s_path = os.path.join(source, file_name)
        d_path = os.path.join(destination, file_name)

        shutil.move(s_path, d_path)
        print(f" {file_name} moved to destination")

print("Task completed, All files moved")
