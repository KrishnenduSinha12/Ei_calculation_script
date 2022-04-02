
echo "Doing Ei calculations"

python Ei.py | bash

wait

echo "Doing gromacs rerun"

bash run_tpr.sh

wait

echo "Doing Energy Calculations"

bash create_xvg.sh

echo "Sorting files"

bash sort_files.sh 

wait

echo "Calculating Average energy"

python Analysis.py
