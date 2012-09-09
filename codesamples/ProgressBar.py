#!/usr/bin/env python
#https://github.com/lunaryorn/snippets/blob/master/python-misc/du.py
#http://love-python.blogspot.dk/2008/05/list-of-files-directories-in-python.html
#count amount of mails in directory

import os

top_level_dir = "../emails"
filecount = 0

def processDirectory ( args, dirname, filenames ):                           
    global filecount
    filecount +=1
        

os.path.walk(top_level_dir, processDirectory, None)
print filecount

