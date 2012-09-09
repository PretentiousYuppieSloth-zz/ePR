import os

top_level_dir = "../codesamples"
counter = 0

for dirName,subdirList,fileList in os.walk( top_level_dir ) :
    for fname in fileList :
        counter +=1

print counter

