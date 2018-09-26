#!/bin/bash
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=2480M

ls sorted*.csv > group_list.txt
python combineOutput.py group_list.txt $1
