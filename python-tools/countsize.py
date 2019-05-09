#!/usr/bin/python

flag = False
total = 0
with open('BinOutput.bin','rb') as f:
	byte = f.read(1)
	while byte != "":
		if flag:
			total += byte
			flag = False
		else:
			flag = True
		byte = f.read(1)

print total
