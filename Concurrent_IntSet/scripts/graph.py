import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def split_contains_ratio(M, n_split):
    M_mean = np.mean(M, axis = 1)
    M_to_plot = np.split(M_mean, n_split)
    return M_to_plot

def plot_contains_ratio(Sync, GL, RWL, PNL, OL, Lazy, Free, X, title, xlabel, titleToSave):
    plt.figure(1, figsize = (12*1.5, 8*1.5), frameon = False)
    plt.title(title, fontsize = 30)
    plt.xlabel(xlabel, fontsize = 15)
    
    plt.plot(X, Sync,"-b", label = "Sync", marker = "*")
    plt.plot(X, GL,"-g", label = "Global", marker = "+")
    plt.plot(X, RWL,"-r", label = "RW", marker = "D")
    plt.plot(X, PNL,"-c", label = "Node", marker = "<")
    plt.plot(X, OL,"-m", label = "Optim", marker = "o")
    plt.plot(X, Lazy,"-y", label = "Lazy", marker = ".")
    plt.plot(X, Free,"-k", label = "Free", marker = "3")
   
    plt.legend(fontsize = 15, loc = 'upper right', ncol=2)

    plt.savefig(titleToSave + ".png")
    plt.show()
    plt.close()
    
#LOAD DATA FROM FILES

#Larger List
matSync_bigger = np.loadtxt('../results/bigger_Synchronized.txt') * 1000
matGL_bigger = np.loadtxt('../results/bigger_GlobalLock.txt') * 1000
matRWL_bigger = np.loadtxt('../results/bigger_GlobalRWLock.txt') * 1000
matPNL_bigger = np.loadtxt('../results/bigger_PerNodeLock.txt') * 1000
matOL_bigger = np.loadtxt('../results/bigger_OptimisticPerNodeLock.txt') * 1000
matLazy_bigger = np.loadtxt('../results/bigger_LazyPerNodeLock.txt') * 1000
matFree_bigger = np.loadtxt('../results/bigger_LockFree.txt') * 1000
#Smaller List
matSync_smaller = np.loadtxt('../results/results_Synchronized.txt') * 1000
matGL_smaller = np.loadtxt('../results/results_GlobalLock.txt') * 1000
matRWL_smaller = np.loadtxt('../results/results_GlobalRWLock.txt') * 1000
matPNL_smaller = np.loadtxt('../results/results_PerNodeLock.txt') * 1000
matOL_smaller = np.loadtxt('../results/results_OptimisticPerNodeLock.txt') * 1000
matLazy_smaller = np.loadtxt('../results/results_LazyPerNodeLock.txt') * 1000
matFree_smaller = np.loadtxt('../results/results_LockFree.txt') * 1000

#Parametres
n_reads = [10, 90, 50, 99];
threads = [1,2,4,6,8,10,12,14,16]

#MAKE AVERAGES AND SPLITS RESULTS

#Larger List
contains_Sync_bigger = split_contains_ratio(matSync_bigger,len(n_reads)-1)
contains_GL_bigger   = split_contains_ratio(matGL_bigger,len(n_reads)-1)
contains_RWL_bigger  = split_contains_ratio(matRWL_bigger,len(n_reads)-1)
contains_PNL_bigger  = split_contains_ratio(matPNL_bigger,len(n_reads)-1)
contains_OL_bigger   = split_contains_ratio(matOL_bigger,len(n_reads)-1)
contains_Lazy_bigger = split_contains_ratio(matLazy_bigger,len(n_reads)-1)
contains_Free_bigger = split_contains_ratio(matFree_bigger,len(n_reads)-1)
#Smaller List
contains_Sync_smaller = split_contains_ratio(matSync_smaller,len(n_reads))
contains_GL_smaller   = split_contains_ratio(matGL_smaller,len(n_reads))
contains_RWL_smaller  = split_contains_ratio(matRWL_smaller,len(n_reads))
contains_PNL_smaller  = split_contains_ratio(matPNL_smaller,len(n_reads))
contains_OL_smaller   = split_contains_ratio(matOL_smaller,len(n_reads))
contains_Lazy_smaller = split_contains_ratio(matLazy_smaller,len(n_reads))
contains_Free_smaller = split_contains_ratio(matFree_smaller,len(n_reads))


#PLOT RESULTS
#Larger List
for i in range(0,len(n_reads)-1):
    plot_contains_ratio( contains_Sync_bigger[i], contains_GL_bigger[i], contains_RWL_bigger[i], contains_PNL_bigger[i], contains_OL_bigger[i], 
     contains_Lazy_bigger[i], contains_Free_bigger[i],threads, "Ops/sec(" + str(n_reads[i]) + "% Reads) List Size - 4000" , "Threads", "../results/4000_" + str(n_reads[i]) +"_reads")
#Smaller list
for i in range(0,len(n_reads)):
    plot_contains_ratio( contains_Sync_smaller[i], contains_GL_smaller[i], contains_RWL_smaller[i], contains_PNL_smaller[i], contains_OL_smaller[i], 
     contains_Lazy_smaller[i], contains_Free_smaller[i],threads, "Ops/sec(" + str(n_reads[i]) + "% Reads) List Size - 256" , "Threads", "../results/256_" + str(n_reads[i]) +"_reads")
    
#PLOT AS CONTAINS INCREASES

#Larger List
matSync_bigger = np.loadtxt('../results/bigger_reads_Synchronized.txt') * 1000
matGL_bigger = np.loadtxt('../results/bigger_reads_GlobalLock.txt') * 1000
matRWL_bigger = np.loadtxt('../results/bigger_reads_GlobalRWLock.txt') * 1000
matPNL_bigger = np.loadtxt('../results/bigger_reads_PerNodeLock.txt') * 1000
matOL_bigger = np.loadtxt('../results/bigger_reads_OptimisticPerNodeLock.txt') * 1000
matLazy_bigger = np.loadtxt('../results/bigger_reads_LazyPerNodeLock.txt') * 1000
matFree_bigger = np.loadtxt('../results/bigger_reads_LockFree.txt') * 1000
#Smaller List
matSync_smaller = np.loadtxt('../results/results_reads_Synchronized.txt') * 1000
matGL_smaller = np.loadtxt('../results/results_reads_GlobalLock.txt') * 1000
matRWL_smaller = np.loadtxt('../results/results_reads_GlobalRWLock.txt') * 1000
matPNL_smaller = np.loadtxt('../results/results_reads_PerNodeLock.txt') * 1000
matOL_smaller = np.loadtxt('../results/results_reads_OptimisticPerNodeLock.txt') * 1000
matLazy_smaller = np.loadtxt('../results/results_reads_LazyPerNodeLock.txt') * 1000
matFree_smaller = np.loadtxt('../results/results_reads_LockFree.txt') * 1000

#Parametres
n_reads = [10, 90, 50, 99];
threads = [1,2,4,6,8,10,12,14,16]
writes_perc = [5,10,20,30,40,50,60,70,80,90]

#MAKE AVERAGES AND SPLITS RESULTS

#Larger List
contains_Sync_bigger = split_contains_ratio(matSync_bigger,len(writes_perc)+1)
contains_GL_bigger   = split_contains_ratio(matGL_bigger,len(writes_perc)+1)
contains_RWL_bigger  = split_contains_ratio(matRWL_bigger,len(writes_perc)+1)
contains_PNL_bigger  = split_contains_ratio(matPNL_bigger,len(writes_perc)+1)
contains_OL_bigger   = split_contains_ratio(matOL_bigger,len(writes_perc)+1)
contains_Lazy_bigger = split_contains_ratio(matLazy_bigger,len(writes_perc)+1)
contains_Free_bigger = split_contains_ratio(matFree_bigger,len(writes_perc)+1)
#Smaller List
contains_Sync_smaller = split_contains_ratio(matSync_smaller,len(writes_perc)+1)
contains_GL_smaller   = split_contains_ratio(matGL_smaller,len(writes_perc)+1)
contains_RWL_smaller  = split_contains_ratio(matRWL_smaller,len(writes_perc)+1)
contains_PNL_smaller  = split_contains_ratio(matPNL_smaller,len(writes_perc)+1)
contains_OL_smaller   = split_contains_ratio(matOL_smaller,len(writes_perc)+1)
contains_Lazy_smaller = split_contains_ratio(matLazy_smaller,len(writes_perc)+1)
contains_Free_smaller = split_contains_ratio(matFree_smaller,len(writes_perc)+1)



plot_contains_ratio(contains_Sync_smaller[1:], contains_GL_smaller[1:], contains_RWL_smaller[1:], contains_PNL_smaller[1:], contains_OL_smaller[1:], 
     contains_Lazy_smaller[1:], contains_Free_smaller[1:], writes_perc, "Ops/sec(16 Threads) List Size - 256", "% writes", "../results/256_16_threads")

plot_contains_ratio(contains_Sync_bigger[1:], contains_GL_bigger[1:], contains_RWL_bigger[1:], contains_PNL_bigger[1:], contains_OL_bigger[1:], 
     contains_Lazy_bigger[1:], contains_Free_bigger[1:], writes_perc, "Ops/sec(16 Threads) List Size - 4000", "% writes", "../results/4000_16_threads")


















    
    
    
    
    