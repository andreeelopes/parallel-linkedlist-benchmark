#!/bin/bash

## all lock implementations
declare -a arr=("Synchronized" "GlobalLock" "GlobalRWLock" "PerNodeLock" "OptimisticPerNodeLock" "LazyPerNodeLock" "LockFree")

for i in "${arr[@]}"
do
	rm "results/bigger_reads_$i.txt"
	echo "$i"
	#percentage of writes
	for r in 0 5 10 20 30 40 50 60 70 80 90
	do
		#number of tries
        for j in 1 2 3 4 5
        do
        	bash ./scripts/intset.sh 1000 16 $r $i >> "results/bigger_reads_$i.txt"       	
        done
        echo "" >> "results/bigger_reads_$i.txt"
	done
done
echo "Test concluded."
