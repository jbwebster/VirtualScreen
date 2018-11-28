# VirtualScreen  

Dr Hansen - Jace Webster  

Made for the Dr Marc Hansen lab at BYU in the PDBIO department, for screening a local library of drug-like molecules against target proteins using AutoDock Vina software. These scripts interact directly with our local library, so any external copies of these scripts (such as that on GitHub) will not work on their own. They rely on a general directory architecture such that drug-like molecules can be found in ./groups/groupXXX/molecule.pdbqt or NATURALPRODUCTS/groups/groupXXX/molecule.pdbqt (for our natural product library). This could of course be changed by updating the hard-coded file paths found within the scripts themselves.

Most of these scripts are run in conjunction by submitting a job to our supercomputer to run the SubmitJobs.sh or NPSubmitJobs.sh. For a more complete explanation of the individual scripts, see the fileExplanations.txt. They are separated into different individual scripts, rather than one or two larger scripts, mainly because there are several actions that are frequently done on an individual, case-by-case basis, so it is helpful to be able to run individual parts of the pipeline when necessary.

