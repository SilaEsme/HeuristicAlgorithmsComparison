import functions
import crossovers
import selections
from enums import enumFunctions, enumCrossovers, enumSelections, enumDecreaseTemp
from algorithms import GeneticAlgorithm as GA, SimulatedAnnealing as SA, GreyWolfOptimization as GWO

dim = 5
iteration_number = 25
functions = enumFunctions.Functions
pop_sizes = [250,500,1000,5000,10000]
num_of_generations = [250, 500, 1000, 1500, 2000]

def run_ga():
    mut_probs =[0.01, 0.02, 0.05, 0.1, 0.15]
    crossover_types = enumCrossovers.Crossovers
    selection_types = enumSelections.Selections

    for func in functions:
        for pop_size in pop_sizes:
            for num_of_gen in num_of_generations:
                for mut_prob in mut_probs:
                    for crossover_type in crossover_types:
                        for selection_type in selection_types:
                            obj_func = functions.selectFunction(func)
                            GA.GA(obj_func, -500, 500, dim, pop_sizes, iteration_number,mut_prob,crossover_type,selection_type)


def run_sa():
    initial_temps = [1000, 5000, 10000]
    decrease_temp_types = enumDecreaseTemp.DecreaseTypes
    for func in functions:
        for initial_temp in initial_temps:
            for decrease_temp_type in decrease_temp_types:
                obj_func = functions.selectFunction(func)
                SA.simulated_annealing(min_values = [-500 for _ in range(dim)], 
                    max_values = [500 for _ in range(dim)],mu = 0, 
                    sigma = 1, initial_temperature = initial_temp,
                    final_temperature = 0.0001, alpha = 0.1, target_function = obj_func, verbose = True, decrease_type = decrease_temp_type)

def run_gwo():
    for func in functions:
        for pop_size in pop_sizes:
            for num_of_gen in num_of_generations:
                obj_func = functions.selectFunction(func)
                GWO.GWO(obj_func, -65536, 65536, dim, 1000, iteration_number)