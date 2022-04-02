
import numpy as np
"""

Use these lines for running the script in Old cray

print("#!/usr/bin/env bash")
print("source /work/chs1/soft/GMX2019.6/bin/GMXRC")

"""
start=1 
stop=129
for j in range (start,stop+1):
       	print ("gmx make_ndx -f md_0_1.gro -o new_index.ndx << EOF \n ri"+" "+str(j)+ " \n 1 &! 18 \n name 18 group1 \n name 19 group2 \n q \nEOF")
       	print("wait")
       	print("gmx grompp -f ie.mdp -c md_0_1.gro -r md_0_1.gro -p topol.top -o rerun_"+str(j)+".tpr -n new_index.ndx -maxwarn 1")
       	print("wait")
        print("rm -rf  topol.tpr *.log *.edr \#new_index.ndx.* ")
       	print("wait")

"""
        print("sed -i 's/rerun_1/topol1/g' q128-gmx2019_1.sh  " )
       	print("wait")
       	print("qsub q128-gmx2019_1.sh  " )
       	print("wait")
       	print("echo 15 16 1 |gmx energy -f topol1.edr -o IE"+"_"+str(j)+".xvg " )
       	print("wait")
        print("rm -rf topol.tpr *.log *.edr \#new_index.ndx.* ")
        print("wait")

"""
