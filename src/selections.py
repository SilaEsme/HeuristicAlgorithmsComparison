import random
import numpy as np

def selectSelection(cbIndex,scores,popSize):
        switcher = {
        0: rouletteWheelSelectionId(scores,popSize),
        1: tournamentSelectionId(scores,popSize),
    }
        return switcher.get(cbIndex, "nothing")

def rouletteWheelSelectionId(scores, popSize):

    reverse = max(scores) + min(scores)
    reverseScores = reverse - scores.copy()
    sumScores = sum(reverseScores)
    pick = random.uniform(0, sumScores)
    current = 0
    for individualId in range(popSize):
        current += reverseScores[individualId]
        if current > pick:
            return individualId

def tournamentSelectionId(scores, popSize):
    m = random. randint(2, popSize)
    scores_randomized = random.choices(scores, k=m)
    best = sorted(scores_randomized)[-1]
    secondbest = sorted(scores_randomized)[-2]
    index_best = np.where(scores == best)[0]
    index_secondbest = np.where(scores == secondbest)[0]
    return index_best, index_secondbest