#! C:/Python32/python -u

#Author: Jace Webster

#Dr Hansen Lab -- 2017 -- BYU

import subprocess
import sys
import operator
import csv

        
def findAffinity(log):
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



try :
   
    config = sys.argv[3]
    listFile = open(sys.argv[1], "r")
    path = "AMPK/AMPK_run3/custom/" # Modify as necessary
    outstring = ""
    for ligand in listFile:
       ligand = path + ligand.rstrip() 
       log = ligand + "_log.txt"
       subprocess.call(["autodock_vina_1_1_2_linux_x86/bin/vina", "--config", config, "--ligand", ligand, "--log", log, "--cpu", "8"])
       affinity = findAffinity(log)
       outstring = outstring + ligand + "," + affinity + "\r\n"
    listFile.close()

    outFile = open(sys.argv[2], "w")
    outFile.write(outstring)
    outFile.close()

    




    
    
#Any exceptions are likely an error in arguments
#or misconfigured files.
except:
    print("Error: USAGE: See README File\nCheck that file names and contents are correct")
