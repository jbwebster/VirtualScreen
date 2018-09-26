#! C:/Python32/python

import sys
from subprocess import call

infile = open(sys.argv[1])
folderInt = int(sys.argv[2])
counter = 0
folderName = "group" + str(folderInt)
directory = "NATURALPRODUCTS/groups/" + folderName
destination = directory + "/"
call(["mkdir", directory])
for line in infile:
    line = line.rstrip()
    mol = "NATURALPRODUCTS/" + line
    if counter < 250:
        call(["mv", mol, destination])
    else:
        folderInt = folderInt + 1
	folderName = "group" + str(folderInt)
	directory = "NATURALPRODUCTS/groups/" + folderName
	destination = directory + "/"
	call(["mkdir", directory])
	call(["mv", mol, destination])
	counter = 0
    counter = counter + 1
infile.close()

