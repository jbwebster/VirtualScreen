#!/bin/bash
#SBATCH --time=00:01:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1240M

python NPCombineOutput.py
