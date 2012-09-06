#http://love-python.blogspot.dk/2008/05/list-of-files-directories-in-python.html

import os

print "\t\tList files in directory:\n"
path = "."
for filenr in os.listdir(path): #list each element in directory
	filepath = os.path.join(path, filenr)
	if os.path.isfile(filepath):   #if we are working with a file.. print the bitch.
		print filepath #print filename


