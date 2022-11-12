def selectSelection(cbIndex,individualLength,parent1,parent2):
        switcher = {
        0: lambda : crossover(individualLength,parent1,parent2),
        1: lambda : twopoint_crossover(individualLength,parent1,parent2),
        2: lambda : uniform_crossover(individualLength,parent1,parent2),
    }
        return switcher.get(cbIndex, "nothing")
