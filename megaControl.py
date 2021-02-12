# Simple program to login and upload files to mega.nz
# Author: Md Tahmid Hossain

from mega import Mega
import cred
from datetime import date
import os, shutil

path = cred.srcPath
dest = cred.destPath
td = date.today()
today = td.strftime('%Y-%m-%d')

mega = Mega()
email= cred.megaEmail
password = cred.megaPass

m = mega.login(email, password)
m.create_folder(today)
folder = m.find(today)

files = os.listdir(path)
files.sort()
i=1
for f in files:
    src = path+f
    m.upload(src, folder[0])
    print(i)
    print('----')
    dst = dest + f
    shutil.move(src, dst)
    i+=1