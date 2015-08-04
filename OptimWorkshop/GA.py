import random
from InitMutFit import *

def GeneticAlgorithm(steps, popsize, distMat, seed):
    ## hardcoded for now, but this is another thing you can tune!
    TOURNAMENTSIZE = 2
    
    random.seed(seed)
    stops = distMat.shape[0]

    ## Initialize population
    parentSols = [InitializeSol(stops) for x in xrange(popsize)]
    parentFits = [Fitness(parent, distMat) for parent in parentSols]
    bestFit = min(parentFits)
    bestSol = parentSols[parentFits.index(bestFit)]
    childSols = [[] for x in xrange(popsize)]
    childFits = [[] for x in xrange(popsize)]
    fitHistory = []

    for i in xrange(steps):
        ## allow population to reproduce
        for j in xrange(popsize):
            winner = Select(parentFits, TOURNAMENTSIZE)
            childSols[j] = Mutate(parentSols[winner])
            childFits[j] = Fitness(childSols[j], distMat)
        ## if we find a new best solution, save it
        if min(childFits) < bestFit:
            bestFit = min(childFits)
            bestSol = childSols[childFits.index(bestFit)]
        ## children become parents for next generation
        parentSols = copy.deepcopy(childSols)
        parentFits = copy.deepcopy(childFits)
        if i % 1000 == 0:
            print bestFit
            fitHistory.append(bestFit)

    return bestSol, fitHistory
