# Unzip all zipped files in a directory
# Author: Md Tahmid Hossain

import zipfile
import os

for root, dirs, files in os.walk("Path"):
    for file in files:
        if file.endswith(".zip"):
            filename = os.path.join(root, file)
            print(filename)
            first= filename.find("\\")
            second = filename.find("\\",first+1, -1)
            folder = filename[:second]
            print(folder)
            print('..............')
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(folder)