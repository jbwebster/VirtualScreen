#! /usr/bin/env python

import sys
import csv
import operator

list = open(sys.argv[1], "r")
out = open("temp.csv", "w")
for line in list:
    line = line.rstrip()
    infile = open(line, "r")
    for currLine in infile:
        currLine = currLine.rstrip()
	if currLine != "":
	    out.write(currLine + "\r\n")
    infile.close()

list.close()
out.close()
out = open(sys.argv[2], "w")
reader = csv.reader(open("temp.csv"), delimiter=",")
sortedList = sorted(reader, key=lambda row: float(row[1]), reverse = False)
outstring = ""
for item in sortedList:
    outstring = item[0] + "," + item[1] + "\r\n"
    out.write(outstring)
out.close()
