#!/bin/bash
rm results.txt

for r in 50 10
do
    for n in 1 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32
    do
        for i in 1 2 3 4 5 6 7 8 9 10
        do
        	bash ./scripts/intset.sh 1000 $n %r >> results.txt        	
        done
    done
done
echo "Test concluded."