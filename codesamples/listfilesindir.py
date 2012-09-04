import os

print "\t\tList files in directory:\n"
path = "graphing-gnuplot"
for file in os.listdir(path): #list each element in directory
	slash = "/"
	filepath = path + slash + file
	if os.path.isfile(filepath):   #if we are working with a file.. print the bitch.
        	print file #print filename


