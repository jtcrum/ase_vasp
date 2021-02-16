#!usr/bin/env python3

import os
import subprocess
import sys
from ase.io import read,write

cwd = os.getcwd()
script = """#!/bin/bash
module load vasp

cd {cwd}

vasp_neb
#end """.format(**locals())

qscript=os.path.join(cwd,'qscript')
f = open(qscript,'w')
f.write(script)
f.close()

q = '*@@schneider_q16copt'
pe = 'mpi-64 64'

cmdlist = 'qsub -o {0} -j y -N {1} -q {2} -pe {3} qscript'.format(cwd,cwd.split('/')[-1],q,pe)

os.system(cmdlist)

