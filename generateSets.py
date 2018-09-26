#! /usr/bin/env python

import sys

infile = open(sys.argv[1], "r")
i = 0
j = 1
outname = "setLists/set" + str(j) + ".txt"
outfile = open(outname, "w")
for line in infile:
    if i < 20:
        outfile.write(line)
	i = i + 1
    else:
        outfile.close()
        j = j + 1
	outname = "setLists/set" + str(j) + ".txt"
	outfile = open(outname, "w")
	outfile.write(line)
	i = 1
outfile.close()
infile.close()
