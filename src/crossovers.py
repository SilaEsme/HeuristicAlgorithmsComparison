import random
import numpy
from algorithms import GeneticAlgorithm as GA

def selectCrossover(cbIndex,individualLength,parent1,parent2):
        switcher = {
        0: crossover(individualLength,parent1,parent2),
        1: twopoint_crossover(individualLength,parent1,parent2),
        2: uniform_crossover(individualLength,parent1,parent2),
    }
        return switcher.get(cbIndex, "nothing")

def crossover(individualLength, parent1, parent2):
    """
    The crossover operator of a two individuals

    Parameters
    ----------
    individualLength: int
        The maximum index of the crossover
    parent1 : list
        The first parent individual of the pair
    parent2 : list
        The second parent individual of the pair

    Returns
    -------
    list
        offspring1: The first updated parent individual of the pair
    list
        offspring2: The second updated parent individual of the pair
    """

    # The point at which crossover takes place between two parents.
    crossover_point = random.randint(0, individualLength - 1)
    # The new offspring will have its first half of its genes taken from the first parent and second half of its genes taken from the second parent.
    offspring1 = numpy.concatenate(
        [parent1[0:crossover_point], parent2[crossover_point:]]
    )
    # The new offspring will have its first half of its genes taken from the second parent and second half of its genes taken from the first parent.
    offspring2 = numpy.concatenate(
        [parent2[0:crossover_point], parent1[crossover_point:]]
    )

    return offspring1, offspring2

#generates two point crossover and returns offsprings
def twopoint_crossover(individualLength, parent1, parent2):
    # The point at which crossover takes place between two parents.
    crossover_point1 = random.randint(0, individualLength - 1)
    crossover_point2 = random.randint(0, individualLength - 1)


    first_point = crossover_point1
    second_point = crossover_point2

    # Must be first point < second point
    # Compare if selected first point bigger than second point

    if(crossover_point1>crossover_point2):
        first_point = crossover_point2
        second_point = crossover_point1
    
    elif(crossover_point1<crossover_point2):
        first_point = crossover_point1
        second_point = crossover_point2


    # The new offspring will have its first half of its genes taken from the first parent and second half of its genes taken from the second parent.
    
    temp_offspring1=numpy.concatenate(
        [parent1[0:first_point], parent2[first_point:second_point]]
    )
    offspring1 = numpy.concatenate(
        ((temp_offspring1), parent1[second_point:]
    ))
    # The new offspring will have its first half of its genes taken from the second parent and second half of its genes taken from the first parent.
    temp_offspring2=numpy.concatenate(
        [parent2[0:first_point], parent1[first_point:second_point]]
    )
    offspring2 = numpy.concatenate(
        ((temp_offspring2), parent2[second_point:]
    ))

    return offspring1, offspring2

def uniform_crossover(crossoverLength,parent1,parent2):
    #generates random mask array
    mask = numpy.random.randint(0,2,crossoverLength)

    offspring1 = [None] * crossoverLength
    offspring2 = [None] * crossoverLength
    for i in range(crossoverLength):
        # if mask index [i] is 0, for offspring1[i]=parent1[i]
        # if mask index [i] is 0, for offspring2[i]=parent2[i]
        if mask[i] == 0:
            offspring1[i] = parent1[i]
            offspring2[i] = parent2[i]
        elif mask[i] == 1:
            offspring1[i] = parent2[i]
            offspring2[i] = parent1[i]


    return offspring1, offspring2