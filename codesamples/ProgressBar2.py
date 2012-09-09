import os

top_level_dir = "../emails"
counter = 0

for dirName,subdirList,fileList in os.walk( top_level_dir ) :
    for fname in fileList:
        print fname
        counter +=1

print counter 