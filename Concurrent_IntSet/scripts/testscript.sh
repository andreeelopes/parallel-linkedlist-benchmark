#!/bin/bash

## all lock implementations
declare -a arr=("Synchronized" "GlobalLock" "GlobalRWLock" "PerNodeLock" "OptimisticPerNodeLock" "LazyPerNodeLock" "LockFree")

for i in "${arr[@]}"
do
	rm "results/results_$i.txt"
done	

#percentage of writes
for r in 50 10 90
do
	for i in "${arr[@]}"
	do
		echo "$i"
		#number of threads
	    for n in 1 2 4 6 8 10 12 14 16
	    do
	    	#number of tries
	        for j in 1 2 3 4 5
	        do
	        	bash ./scripts/intset.sh 1000 $n $r $i >> "results/results_$i.txt"       	
	        done
	        echo "" >> "results/results_$i.txt"
	    done
	done
done
echo "Test concluded."
