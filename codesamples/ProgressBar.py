#!/usr/bin/env python

#count amount of mails in directory

import os

top_level_dir = "../"


def processDirectory ( args, dirname, filenames ):
    global path                            
    path = dirname
 
    for filenr in os.listdir(path): #list each element in directory
        slash = "/"
        filepath = path + slash + filenr
        if os.path.isfile(filepath):   #if we are working with a file.. print the bitch.
            print filepath #print filename
            


os.path.walk(top_level_dir, processDirectory, None)
