#!/bin/bash ##Specify the shell from tcsh,bash,zsh etc

#SBATCH -p node ##Options of node, seseml, sesempi, sesebig
#SBATCH -n 4 ##Set number of processors needed for the job
#SBATCH --mem 70GB ##Set total RAM required
#SBATCH --time=1-00:00:00 ##Set time needed for the job
#SBATCH --mail-type=BEGIN ##Specify the type of job execution emails you need like beginning, failing or end of job.
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=END
#SBATCH --mail-user=johntl3@illinois.edu ##Specify your email where the information about the execution will be sent.

module load libRadtran-2.0.4

echo "#####################################################" ##This is to print any info about the job
echo "# Welcome to the libRadtran runner"
echo "#####################################################"

###export OMP_NUM_THREADS=1 ##This is to specify how many threads you need per processor.

uvspec <brightness_afglms.inp> brightness_afglms.out
uvspec <brightness_afglmw.inp> brightness_afglmw.out
uvspec <brightness_afglss.inp> brightness_afglss.out
uvspec <brightness_afglsw.inp> brightness_afglsw.out
uvspec <brightness_afglt.inp> brightness_afglt.out
uvspec <brightness_afglus.inp> brightness_afglus.out

echo "DONE!"
