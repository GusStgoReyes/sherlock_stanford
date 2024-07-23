#!/bin/bash
#SBATCH --job-name=efficient_analysis
#SBATCH --output=sbatch_outputs/inefficient_analysis_%A_%a.out
#SBATCH --error=sbatch_outputs/inefficient_analysis_%A_%a.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=16G
#SBATCH --time=0:30:00
#SBATCH -p normal
#SBATCH --mail-type=FAIL
#SBATCH --array=0-200

# Activate your virtual environment if needed
source /scratch/users/gustxsr/sherlock_stanford/myenv/bin/activate

# Run your Python script
python /scratch/users/gustxsr/sherlock_stanford/3_analysis_inefficient.py $SLURM_ARRAY_TASK_ID