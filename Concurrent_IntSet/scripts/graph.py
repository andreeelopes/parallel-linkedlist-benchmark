

import numpy as np
import matplotlib.pyplot as plt


matSync = np.loadtxt('../results_Synchronized.txt')
matGL = np.loadtxt('../results_GlobalLock.txt')
matRWL = np.loadtxt('../results_GlobalRWLock.txt')
matPNL = np.loadtxt('../results_PerNodeLock.txt')
matOL = np.loadtxt('../results_OptimisticPerNodeLock.txt')
matLazy = np.loadtxt('../results_LazyPerNodeLock.txt')
#matFree = np.loadtxt('../results_LockFree.txt')


def splitToShow(M):
    M_mean = np.mean(M, axis = 1)
    M_contains_perc = np.split(M_mean, 2)
    return M_contains_perc[0], M_contains_perc[1]

def plot(Sync, GL, RWL, PNL, OL, Lazy, Free, title, xlabel, ylabel):
    plt.figure(1, figsize = (12,8), frameon = False)
    plt.title(title, fontsize = 50)
    plt.xlabel(xlabel, fontsize = 25)
    plt.ylabel(ylabel, fontsize = 25)
    
    plt.plot(range(1,34,2), Sync,"-b", label = "Sync", marker = "*")
    plt.plot(range(1,34,2), GL,"-g", label = "Global", marker = "+")
    plt.plot(range(1,34,2), RWL,"-r", label = "RW", marker = "D")
    plt.plot(range(1,34,2), PNL,"-c", label = "Node", marker = "<")
    plt.plot(range(1,34,2), OL,"-m", label = "Optim", marker = "o")
    plt.plot(range(1,34,2), Lazy,"-y", label = "Lazy", marker = ".")
    plt.plot(range(1,34,2), Free,"-k", label = "Free", marker = "3")
    
    plt.legend(fontsize = 20)
    
    plt.savefig(title + ".png")
    plt.show()
    plt.close()

contains50_Sync, contains10_Sync = splitToShow(matSync)
contains50_GL, contains10_GL = splitToShow(matGL)
contains50_RWL, contains10_RWL = splitToShow(matRWL)
contains50_PNL, contains10_PNL = splitToShow(matPNL)
contains50_OL, contains10_OL = splitToShow(matOL)
contains50_Lazy, contains10_Lazy = splitToShow(matLazy)
#contains50_Free, contains10_Free = splitToShow(matFree)

plot( contains10_Sync, contains10_GL, contains10_RWL, contains10_PNL, contains10_OL, 
     contains10_Lazy, range(1,18), "90% reads", "Threads", "Ops/sec")

plot( contains50_Sync, contains50_GL, contains50_RWL, contains50_PNL, contains50_OL, 
     contains50_Lazy, range(1, 18), "50% reads", "Threads", "Ops/sec")

    
    
    
    
    
    
    