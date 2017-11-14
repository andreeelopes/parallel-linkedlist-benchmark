#!/bin/bash

## all lock implementations
declare -a arr=("Synchronized" "GlobalLock" "GlobalRWLock" "PerNodeLock" "OptimisticPerNodeLock" "LazyPerNodeLock" "LockFree")

for i in "${arr[@]}"
do
	echo "$i"
	#percentage of writes
	for r in 0 10 20 30 40 50 60 70 80 90
	do
		#number of tries
        for j in 1 2 3 4 5
        do
        	bash ./scripts/intset.sh 1000 32 $r $i >> "results_reads_$i.txt"       	
        done
        echo "" >> "results_reads_$i.txt"
	done
done
echo "Test concluded."