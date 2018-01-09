import os
import fnmatch
def findfile(inputdir):
    txtlist = []
    for parent, dirnames, filename in os.walk(inputdir):
        for filenames in filename:
            txtlist.append(filenames)
    return fnmatch.filter(txtlist, '*.png')
m=findfile('世界最佳球衣')
print(m)
