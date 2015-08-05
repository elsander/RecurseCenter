import random
import math
from InitMutFit import *

def SimulatedAnnealing(steps, placeholder, distMat, seed):
    ## hardcoded
    STARTTEMP = 5
    ENDTEMP = .001
    
    random.seed(seed)
    stops = distMat.shape[0]
    ## Randomly generate our starting point
    bestSol = InitializeSol(stops)
    bestFit = Fitness(bestSol, distMat)
    currSol = bestSol
    currFit = bestFit
    fitHistory = []

    ## uniform cooling schedule based on number of steps
    ## There are lots of other strategies for cooling the chain
    ## but this is nice and simple
    deltat = (STARTTEMP - ENDTEMP)/steps
    temp = STARTTEMP

    for i in xrange(steps):
        ## try several steps
        trialSol = Mutate(bestSol)
        trialFit = Fitness(trialSol, distMat)
        ## if trialFit is better (less than) currFit, it will always
        ## be accepted. Otherwise, accept with probability related
        ## to the temperature.
        probAccept = math.exp((currFit - trialFit)/temp)
        if random.random() <= probAccept:
            currFit = trialFit
            currSol = trialSol
            ## update best solution if appropriate
            if currFit < bestFit:
                bestFit = currFit
                bestSol = currSol
            
        if i % 1000 == 0:
            print bestFit
            fitHistory.append(bestFit)
        ## update temperature
        temp = temp - deltat
    return bestSol, fitHistory
