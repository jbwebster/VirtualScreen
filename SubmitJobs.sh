#!/bin/bash
id=$(sbatch -a 1-45 JobScript.sh $1 | awk '{print $4}')
id2=$(sbatch --dependency=afterok:$id PrepOutput.sh $2 | awk '{print $4}')
sbatch --dependency=afterok:$id2 collectHits.sh $2
