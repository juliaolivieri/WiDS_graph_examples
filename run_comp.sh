#!/bin/bash
#
#SBATCH --job-name=graph
#SBATCH --output=graph.%j.out
#SBATCH --error=graph.%j.err
#SBATCH --time=24:00:00
##SBATCH --qos=normal
#SBATCH -p owners
##SBATCH -p normal
#SBATCH --nodes=1
#SBATCH --mem=20G
date
NAME="web-BerkStan"
#NAME="mouse_gene"
a="python -u compare_graphs.py --name ${NAME}"
echo $a 
eval $a
date
