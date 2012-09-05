import os

print "\t\tList files in directory:\n"
path = "../emails/._dep.gd@syriantelecom.sy"
for filenr in os.listdir(path): #list each element in directory
	slash = "/"
	filepath = path + slash + filenr
	if os.path.isfile(filepath):   #if we are working with a file.. print the bitch.
		print filepath #print filename


