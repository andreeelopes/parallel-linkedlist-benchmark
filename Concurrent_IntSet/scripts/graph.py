import numpy as np
import matplotlib.pyplot as plt

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


#PLOT HIGH AND LOW CONTAINS RATIO

matSync = np.loadtxt('../results/results_Synchronized.txt') * 1000
matGL = np.loadtxt('../results/results_GlobalLock.txt') * 1000
matRWL = np.loadtxt('../results/results_GlobalRWLock.txt') * 1000
matPNL = np.loadtxt('../results/results_PerNodeLock.txt') * 1000
matOL = np.loadtxt('../results/results_OptimisticPerNodeLock.txt') * 1000
matLazy = np.loadtxt('../results/results_LazyPerNodeLock.txt') * 1000
matFree = np.loadtxt('../results/results_LockFree.txt') * 1000


contains_Sync = split_contains_ratio(matSync,3)
contains_GL = split_contains_ratio(matGL,3)
contains_RWL = split_contains_ratio(matRWL,3)
contains_PNL = split_contains_ratio(matPNL,3)
contains_OL = split_contains_ratio(matOL,3)
contains_Lazy = split_contains_ratio(matLazy,3)
contains_Free = split_contains_ratio(matFree,3)
threads = [1,2,4,6,8,10,12,14,16]

plot_contains_ratio( contains_Sync[2], contains_GL[2], contains_RWL[2], contains_PNL[2], contains_OL[2], 
     contains_Lazy[2], contains_Free[2],threads, "Ops/sec(10% Reads)", "Threads", "../results/Ops_sec_10_reads")

plot_contains_ratio( contains_Sync[1], contains_GL[1], contains_RWL[1], contains_PNL[1], contains_OL[1], 
     contains_Lazy[1], contains_Free[1], threads, "Ops/sec(90% Reads)", "Threads", "../results/Ops_sec_90_reads")

plot_contains_ratio( contains_Sync[0], contains_GL[0], contains_RWL[0], contains_PNL[0], contains_OL[0], 
     contains_Lazy[0], contains_Free[0],threads, "Ops/sec(50% Reads)", "Threads", "../results/Ops_sec_50_reads")

    
#PLOT AS CONTAINS INCREASES

matSync = np.loadtxt('../results/results_reads_Synchronized.txt')
matGL = np.loadtxt('../results/results_reads_GlobalLock.txt')
matRWL = np.loadtxt('../results/results_reads_GlobalRWLock.txt')
matPNL = np.loadtxt('../results/results_reads_PerNodeLock.txt')
matOL = np.loadtxt('../results/results_reads_OptimisticPerNodeLock.txt')
matLazy = np.loadtxt('../results/results_reads_LazyPerNodeLock.txt')
matFree = np.loadtxt('../results/results_reads_LockFree.txt')


contains_Sync = split_contains_ratio(matSync,10)
contains_GL = split_contains_ratio(matGL,10)
contains_RWL = split_contains_ratio(matRWL,10)
contains_PNL = split_contains_ratio(matPNL,10)
contains_OL = split_contains_ratio(matOL,10)
contains_Lazy = split_contains_ratio(matLazy,10)
contains_Free = split_contains_ratio(matFree,10)


plot_contains_ratio(contains_Sync, contains_GL, contains_RWL, contains_PNL, contains_OL, 
     contains_Lazy, contains_Free, range(0,100,10), "Ops/sec(32 Threads)", "% contains", "../results/Ops_sec_32_threads")


















    
    
    
    
    