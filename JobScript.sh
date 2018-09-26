#!/bin/bash
#SBATCH --time=8:00:00
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=2480M
SET="setLists/set"$SLURM_ARRAY_TASK_ID".txt"
OUTFILE="set"$SLURM_ARRAY_TASK_ID".csv"
CONFIG=$1
python PerformScreen.py $SET $OUTFILE $CONFIG
