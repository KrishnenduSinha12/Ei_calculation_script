for val in {1..129}
    do 
        echo "Coul-SR:group1-group2\nLJ-SR:group1-group2" 0 |gmx energy -f rerun_$val.edr -o Ei_$val.xvg 
    done
wait

for val in {10..99}
do
        mv Ei_$val.xvg Ei_0$val.xvg
done
wait

for val in {1..9}
do
        mv Ei_$val.xvg Ei_00$val.xvg
done
wait
