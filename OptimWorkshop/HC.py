import random
from InitMutFit import *

def HillClimber(steps, tryPerStep, distMat, seed):
    random.seed(seed)
    stops = distMat.shape[0]
    ## Randomly generate our starting point
    bestSol = InitializeSol(stops)
    bestFit = Fitness(bestSol, distMat)

    ## Initialize data structure for trial solutions and fitnesses
    trialSols = [[] for x in xrange(tryPerStep)]
    trialFits = [[] for x in xrange(tryPerStep)]
    fitHistory = []
    
    for i in xrange(steps):
        ## try several steps
        for j in xrange(tryPerStep):
            trialSols[j] = Mutate(bestSol)
            trialFits[j] = Fitness(trialSols[j], distMat)
        ## is the best trial solution better than our current best?
        ## If so, replace. Otherwise, move to next step
        ## Note that we are minimizing here
        if min(trialFits) < bestFit:
            bestFit = min(trialFits)
            bestSol = trialSols[trialFits.index(bestFit)]
        if i % 1000 == 0:
            print bestFit
            fitHistory.append(bestFit)
    return bestSol, fitHistory
