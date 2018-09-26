#! C:/Python32/python -u

#Author: Jace Webster

#Dr Hansen Lab -- 2017 -- BYU

import subprocess
import sys
import operator
import csv

# --------- Batch Class ----------------
# One Batch object will be made for each
# directory of molecules to be analyzed
# The use of a class here for the brute
# force screen probably isn't necessary,
# but... copy and paste is too great
# to pass up.
# --------------------------------------
class Batch(object):
    #Constructor
    def __init__(self, folderName):
        self.folderName = folderName
        self.outString = ""


    def analyzeBatch(self, config):
        listName = self.folderName + "/list.txt"
        listFile = open(listName, "r")
        for line in listFile:
	    if ("list.txt" != line.rstrip()):
                moleculePath = self.folderName + "/" + line.rstrip()
                log = moleculePath + "_log.txt"
                sys.stdout.flush()
		try:
                    subprocess.call(["autodock_vina_1_1_2_linux_x86/bin/vina", "--config", config, "--ligand", moleculePath, "--log", log, "--cpu", "8"])
		except:
		    print("Error docking " + moleculePath) 
                affinity = self.findAffinity(log)
                self.outString = self.outString + moleculePath + "," + affinity + "\r\n"
        listFile.close()
        
    def findAffinity(self, log):
        try:
            logfile = open(log, "r")
            keepGoing = True
	    while keepGoing:
	        temp = logfile.readline()
	        if temp[0] == "-":
	            keepGoing = False
	    temp = logfile.readline()
        
            values = temp.split()
            logfile.close()
            return values[1]
        except:
	    return 0 

    def toString(self):
        return self.outString

    def getFolderName(self):
        return self.folderName


# -----End of Batch Class------------


#Main code
#NPScreen will be a brute force screen,
#Rather than using a sorting algorithm

try :
    groupName = sys.argv[1]
    location = "NATURALPRODUCTS/groups/" + groupName
    batch = Batch(location)

    config = sys.argv[3]

    try:
        batch.analyzeBatch(config)
    except:
        print("")
            
    
    outFile = open(sys.argv[2], "w")
    outFile.write(batch.toString())
    outFile.close()

    #Now sort the csv file and reprint it in a sorted format
    
    reader = csv.reader(open(sys.argv[2]), delimiter=",")
    sortedList = sorted(reader, key=lambda row: float(row[1]), reverse=False)
    sortedFileName = "sorted_" + sys.argv[2]
    sortedOut = open(sortedFileName, "w")
    outstring = ""
    for item in sortedList:
        outstring = outstring + item[0] + "," + item[1] + "\n"
    sortedOut.write(outstring)
    sortedOut.close()
    
    
#Any exceptions are likely an error in arguments
#or misconfigured files.
except:
    print("Error: USAGE: See README File\nCheck that file names and contents are correct")
