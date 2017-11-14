#!/bin/sh 
java="java -enableassertions -verbose:gc -Xms1024M"

warmup=2000
duration=${1}
nr_threads=${2:-1}
write_perc=${3:-50}
list_impl=${4}

value_range=262144
initial_size=256


${java} -cp bin cp.benchmark.Driver -d ${duration} -w ${warmup} -n ${nr_threads} \
                cp.benchmark.intset.Benchmark ${list_impl} \
                -r ${value_range} -i ${initial_size} -w ${write_perc}
