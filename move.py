# Moves files from one directory to another
# Author: Md Tahmid Hossain

import os, shutil
import cred

srcPath = cred.srcPath
destPath = cred.destPath

files = os.listdir(srcPath)
files.sort()
for f in files:
    src = srcPath+f
    dst = destPath+f
    shutil.move(src,dst)