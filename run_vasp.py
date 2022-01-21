#!usr/bin/env python3

import os
import subprocess
import sys
from ase.io import read,write

q = '*@@schneider_q16copt'
pe = 'mpi-64'
nprocs =' 64'

cwd = os.getcwd()
script = """#!/bin/bash
module load vasp

cd {cwd}

mpirun -np {nprocs} vasp_neb
#end """.format(**locals())

qscript=os.path.join(cwd,'qscript')
f = open(qscript,'w')
f.write(script)
f.close()



cmdlist = 'qsub -o {0} -j y -N {1} -q {2} -pe {3} {4} qscript'.format(cwd,cwd.split('/')[-1],q,pe,nprocs)

os.system(cmdlist)

