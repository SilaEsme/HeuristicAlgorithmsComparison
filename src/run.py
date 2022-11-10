import functions
from enumFunctions import Functions
from algorithms import GeneticAlgorithm as GA
from algorithms import GreyWolfOptimization as GWO
from algorithms import SimulatedAnnealing as SA

def Call_Algorithm():
    functionIndex = Functions.schwefel
    obj_func = functions.selectFunction(Functions.schwefel)
    # dim array size, -5 lb +5 lb 
    # GWO.GWO(obj_func, -65536, 65536, 30, 1000, 250)
    #SA.simulated_annealing( min_values = [-500,-500,-500,-500,-500,-500,-500,-500,-500], max_values = [500,500,500,500,500,500,500,500,500], mu = 0, sigma = 1, initial_temperature = 1.0, temperature_iterations = 100,
    #    final_temperature = 0.0001, alpha = 0.9, target_function = obj_func, verbose = True)
    GA.GA(obj_func, -500, 500, 7, 10, 25)

def main():
    Call_Algorithm()

if __name__ == "__main__":
    main()