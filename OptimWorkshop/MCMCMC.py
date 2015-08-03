import random
from InitMutFit import *
import pdb

def InitializeTemps(maxtemp, mintemp, nchains):

def TrySwap(hotFit, coldFit, hotTemp, coldTemp):
    ## MATH GOES HERE

def MCMCMC(steps, nchains, distMat, seed):
    ##hardcoded, but these can also be tuned!
    SWAPSTEPS = 20
    MAXTEMP = 5
    MINTEMP = .001

    random.seed(seed)
    stops = distMat.shape[0]

    ## Initialize temperatures and chains
    temps = InitializeTemps(MAXTEMP, MINTEMP, nchains)
    chains = [InitializeSol(stops) for x in xrange(nchains)]
    fits = [Fitness(chain, distMat) for chain in chains]
    bestFit = min(chains)
    bestSol = chains[fits.index(bestFit)]

    for i in xrange(steps):
        ## swap chains
        if i % SWAPSTEPS == 0:
            for j in xrange(1, stops):
                flag = TrySwap(fits[i], fits[j], temps[i], temps[j])
                if flag:
                    chains[i], chains[j] = chains[j], chains[i]
                    fits[i], fits[j] = fits[j], fits[i]
        ## let each chain take a step
        for j in xrange(stops):
            trialSol = Mutate(chains[j])
            trialFit = Fitness(trialSol, distMat)
            probAccept = math.exp((fits[j] - trialFit)/temps[j])
            if random.random() <= probAccept:
                fits[j] = trialFit
                chains[j] = trialSol
                ## update best solution if appropriate
                if trialFit < bestFit:
                    bestFit = trialFit
                    bestSol = trialSol

        if i % 1000 == 0:
            print bestFit
            
    return bestSol
