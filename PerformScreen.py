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
# --------------------------------------
class Batch(object):
    #Constructor
    def __init__(self, folderName):
        self.folderName = folderName
        self.outString = ""
        self.average = 0.0
        self.mod = 0
        self.docked = []
        self.sumTotal = 0
        self.analyzed = 0


    def analyzePartOfBatch(self, config):
        listName = self.folderName + "/list.txt"
        listFile = open(listName, "r")
        currLine = 0
        dockDueToHit = False
        for line in listFile:
            #Originally was currLine % 10. Changed to 40 for testing
            if (line.rstrip() != "list.txt" and currLine % 40 == self.mod and currLine not in self.docked) or (dockDueToHit and currLine not in self.docked):
                moleculePath = self.folderName + "/" + line.rstrip()
                log = moleculePath + "_log.txt"
                sys.stdout.flush()
                subprocess.call(["autodock_vina_1_1_2_linux_x86/bin/vina", "--config", config, "--ligand", moleculePath, "--log", log, "--cpu", "8"])
                affinity = self.findAffinity(log)
                self.outString = self.outString + moleculePath + "," + affinity + "\r\n"
                self.sumTotal = self.sumTotal + float(affinity)
                self.analyzed = self.analyzed + 1
                self.docked.append(currLine)
                if float(affinity) < -8.5:
                    dockDueToHit = True
                else:
                    dockDueToHit = False
            currLine = currLine + 1
            
        self.average = float(self.sumTotal) / float(self.analyzed)
        self.mod = self.mod + 3
        listFile.close()
        
    def findAffinity(self, log):
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

    def toString(self):
        return self.outString

    def getFolderName(self):
        return self.folderName

    def getAverage(self):
        return self.average

# -----End of Batch Class------------


#Main code

# Sorting function, based on average affinity
# of all docked molecules in a Batch
def bubbleSort(Batches):
    exchanges = True
    passnum = len(Batches) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            firstB = Batches[i]
            secondB = Batches[i+1]
            if firstB.getAverage() > secondB.getAverage():
                exchanges = True
                temp = Batches[i]
                Batches[i] = Batches[i+1]
                Batches[i+1] = temp
        passnum = passnum - 1



#Start here
try :
    #Create Batch objects
    Batches = []
    listFile = open(sys.argv[1], "r")
    for line in listFile:
        groupName = line.rstrip()
        if line != "":
            location = "groups/" + groupName
            batch = Batch(location)
            Batches.append(batch)
    listFile.close()

    #Get config file
    config = sys.argv[3]

    #Sample each Batch
    for group in Batches:
        try:
            group.analyzePartOfBatch(config) 
        except:
            print("")
            


    count = 0
    #Originally was count < 19. Changed to count < 5 for testing purposes
    while count < 5:
        count = count + 1
        if len(Batches) > 2:
            bubbleSort(Batches)
        try:
            Batches[0].analyzePartOfBatch(config)
        except:
            print("")
        if len(Batches) > 1:
            try:
                Batches[1].analyzePartOfBatch(config)
            except:
                print("")



    
    outFile = open(sys.argv[2], "w")
    for group in Batches:
        outFile.write(group.toString())
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
