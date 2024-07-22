#!/bin/bash
#SBATCH --job-name=inefficient_analysis
#SBATCH --output=sbatch_outputs/inefficient_analysis.out
#SBATCH --error=sbatch_outputs/inefficient_analysis.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=0:30:00
#SBATCH -p normal
#SBATCH --mail-type=FAIL

# Activate your virtual environment if needed
# source /scratch/users/gustxsr/sherlock_stanford/myenv/bin/activate

# Run your Python script
python /scratch/users/gustxsr/sherlock_stanford/3_analysis_inefficient.py