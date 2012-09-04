To read a file use:
	1.	fileHandle = open ( 'text.txt', 'r' )
	2.	str1 = fileHandle.read()
	3.	fileHandle.close()
	4.	print str1
	5.	break
 To write data to a file use:
	1.	fileHandle = open ( 'text.txt', 'w' )
	2.	fileHandle.write(str1)
	3.	fileHandle.close()
 To append data to an existing file use:
	1.	fileHandle = open ( 'text.txt', 'a' )
	2.	fileHandle.write(str1)
	3.	fileHandle.close()
