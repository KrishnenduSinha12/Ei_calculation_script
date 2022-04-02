for i in {1..129}
do
	gmx mdrun -v -deffnm rerun_$i -rerun md_0_1_noPBC.xtc
	wait 
done

