#! C:/Python32/python

import sys
from subprocess import call

infile = open(sys.argv[1], "r")
i = 0
for line in infile:
    mol = line.split(",")[0] 
    mol_out = mol.split(".")[0] + "_out.pdbqt"
    if (mol.split("/")[0] == "NATURALPRODUCTS"):
        molecule_in = mol.split("/")[3] 
    else:
        molecule_in =  mol.split("/")[2]
	
    mol_name = molecule_in.split(".")[0]
    molecule_out = mol_name + "_out.pdbqt"

    if i < 100:
        dest = "TOP100/" + molecule_in
        call(["cp", mol, dest])
    elif i >= 100 and i < 200:
        dest = "101_200/" + molecule_in
        call(["cp", mol, dest])
    if i < 200:
        dest_out = "HIT_OUTFILES/" + molecule_out
	call(["cp", mol_out, dest_out])
    i = i + 1
        
