"""
sga.py
Morgan Bauer
22 February 2024

Homework 01 for CS-470 Evolutionary Computation
An object-oriented implementation of the Simple Genetic Algorithm (SGA).
Parameters are read from the command line: maximum generation number, population
size, probability of crossover, probability of mutation, string length, and an
exponent used in certain fitness functions.

Example: python3 sga.py 20 100 0.03 0.01 30 10

pledged
"""
from population import Population
from sga_stats import stats, report
from objective_funcs import objective_func_1, objective_func_2, objective_func_3
import sys

def main():
    """Executes the SGA"""
    # Read parameters from the command line
    max_gen = int(sys.argv[1])
    pop_size = int(sys.argv[2])
    pc = float(sys.argv[3])
    pm = float(sys.argv[4])
    string_length = int(sys.argv[5])
    objective_function = objective_func_3  # Note that for now, the objective
                                           # function is being maximized, there
                                           # is not a separate fitness function
    n = int(sys.argv[6])
    gen_num = 0

    while gen_num < max_gen:
        gen_num += 1

        # Initialize first generation
        if gen_num == 1:
            generation = Population(pop_size, [], pc, pm, string_length,
                                    objective_function, n)

        # Generate statistics and create a new generation
        generation.evaluate_fitness()
        gen_stats = stats(generation)
        report(generation, gen_num)
        generation = generation.new_generation()

if __name__ == "__main__":
    main()