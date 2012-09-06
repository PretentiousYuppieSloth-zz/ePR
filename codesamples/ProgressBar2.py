import os

path = "."
dir_count = 0
file_count = 0

for pathname, dirnames, filenames in os.walk(path):
    for filenr in os.listdir(path): #list each element in directory
        filepath = os.path.join(pathname, filenr)
        if os.path.isfile(filepath):   #if we are working with a file.. print the bitch.
            #print filepath #print filename
            file_count += len(filepath)

print file_count

#print file_count