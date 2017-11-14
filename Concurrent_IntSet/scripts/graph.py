import numpy as np
import matplotlib.pyplot as plt

def split_contains_ratio(M, n_split):
    M_mean = np.mean(M, axis = 1)
    M_to_plot = np.split(M_mean, n_split)
    return M_to_plot

def plot_contains_ratio(Sync, GL, RWL, PNL, OL, Lazy, Free, X, title, xlabel, titleToSave):
    plt.figure(1, figsize = (12,8), frameon = False)
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

matSync = np.loadtxt('../results/results_Synchronized.txt')
matGL = np.loadtxt('../results/results_GlobalLock.txt')
matRWL = np.loadtxt('../results/results_GlobalRWLock.txt')
matPNL = np.loadtxt('../results/results_PerNodeLock.txt')
matOL = np.loadtxt('../results/results_OptimisticPerNodeLock.txt')
matLazy = np.loadtxt('../results/results_LazyPerNodeLock.txt')
matFree = np.loadtxt('../results/results_LockFree.txt')


contains_Sync = split_contains_ratio(matSync,2)
contains_GL = split_contains_ratio(matGL,2)
contains_RWL = split_contains_ratio(matRWL,2)
contains_PNL = split_contains_ratio(matPNL,2)
contains_OL = split_contains_ratio(matOL,2)
contains_Lazy = split_contains_ratio(matLazy,2)
contains_Free = split_contains_ratio(matFree,2)

plot_contains_ratio( contains_Sync[1], contains_GL[1], contains_RWL[1], contains_PNL[1], contains_OL[1], 
     contains_Lazy[1], contains_Free[1], range(1,34,2), "Ops/sec(90% Reads)", "Threads", "../results/Ops_sec_90_reads")

plot_contains_ratio( contains_Sync[0], contains_GL[0], contains_RWL[0], contains_PNL[0], contains_OL[0], 
     contains_Lazy[0], contains_Free[0], range(1,34,2), "Ops/sec(50% Reads)", "Threads", "../results/Ops_sec_50_reads")

    
    
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


















    
    
    
    
    