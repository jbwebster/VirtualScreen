#!/bin/bash
#SBATCH --time=5:00:00
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=1240M
SETFILE="group"$SLURM_ARRAY_TASK_ID
OUTFILE="group"$SLURM_ARRAY_TASK_ID".csv"
CONFIG=$1
python NPScreen.py $SETFILE  $OUTFILE $CONFIG
