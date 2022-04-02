#Create dirs for tpr edr and xvg files
mkdir tprs edrs xvgs

# move the files to dirs
mv rerun_*.tpr tprs
mv rerun_*.edr edrs
mv Ei_*.xvg xvgs

# delete all log files

rm -rf rerun_*.log

 
