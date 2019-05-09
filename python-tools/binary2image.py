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

for filepath in glob.glob("{}*".format(sys.argv[1])):
	filename = os.path.basename(filepath)

	print("converting {} to {}.pgm".format(filename, filename))
	#print('{}{}'.format(sys.argv[2],filename))
	bitout = open(filepath, 'rb')
	img = bitout.read()
	bitout.close()
	Image.frombytes('L', (256,256), img).save('{}{}.pgm'.format(sys.argv[2],filename))
print("Converted all binaries in {} to pictures strings in folder {}".format(sys.argv[1],sys.argv[2]))