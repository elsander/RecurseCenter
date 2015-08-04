from TravelingSalesperson import *
import pdb
import scipy
import pylab as pl

## function to plot swap probability through time
## plot best solution fitness through time

def PlotMultipleRuns(Alg, nruns = 20, fname = None):
    if fname:
        runs = scipy.genfromtxt(fname)
    else:
        runs = []
        for i in xrange(nruns):
            bestSol, fitHistory = TSP(200, Alg, 20000, 30, seed = None,
                                      coordfile = 'tmp.txt')
            runs.append(fitHistory)
        fname = 'MultRuns-' + str(Alg) + '.txt'
        runs = scipy.array(runs)
        scipy.savetxt(fname, runs)

    ## plotting
    Xs = range(0, runs.shape[0]*1000, 1000)
    for i in xrange(runs.shape[0]):
        pl.plot(Xs, runs[i,:])
    pl.show()

def LongMC3(fname = None):
    if fname:
        run = scipy.genfromtxt(fname)
    else:
        bestSol, run = TSP(200, 'MC3', 200000, 10, seed = None,
                                  coordfile = 'tmp.txt')
        fname = 'MultRuns-MC3-Long.txt'
        run = scipy.array(run)
        scipy.savetxt(fname, run)

    ## plotting
    Xs = range(0, run.shape[0]*1000, 1000)
    pl.plot(Xs, run)
    pl.show()
    
