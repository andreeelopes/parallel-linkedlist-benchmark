#!/bin/bash

## all lock implementations
declare -a arr=("Synchronized" "GlobalLock" "GlobalRWLock" "PerNodeLock" "OptimisticPerNodeLock" "LazyPerNodeLock" "LockFree")

for i in "${arr[@]}"
do
	rm "results/results_$i.txt"
	echo "$i"
	#percentage of writes
	for r in 50 10
	do
		#number of threads
	    for n in 1 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32
	    do
	    	#number of tries
	        for j in 1 2 3 4 5
	        do
	        	bash ./scripts/intset.sh 3000 $n $r $i >> "results/results_$i.txt"       	
	        done
	        echo "" >> "results/results_$i.txt"
	    done
	done

done
echo "Test concluded."
