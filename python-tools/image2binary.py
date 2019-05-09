#!/usr/bin/python
try:
    from PIL import Image
except ImportError:
    import Image
import sys
import glob
import os


if len(sys.argv) < 3:
    print("usage: image2binary <source-folder> <dest-folder>")
    exit()

for filepath in glob.glob("{}*.pgm".format(sys.argv[1])):
    filename, file_extension = os.path.splitext(os.path.basename(filepath))

    print("converting {}{} to {}".format(filename, file_extension,filename))
    #print('{}{}'.format(sys.argv[2],filename))
    img = Image.open('{}'.format(filepath)).convert('L').tobytes()
    bitout = open('{}{}'.format(sys.argv[2],filename), 'w+')
    bitout.write(img)
    bitout.close()
print("Converted all pictures in {} to binary strings in folder {}".format(sys.argv[1],sys.argv[2]))