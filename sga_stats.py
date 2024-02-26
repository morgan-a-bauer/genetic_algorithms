"""
sga_stats.py
Morgan Bauer
23 February 2024

Homework 01 for CS-470 Evolutionary Computation
Statistics and output for the implementation of the Simple Genetic algorithm in
sga.py
"""
from population import Population
from numpy import where

def stats(pop: Population):
    """Generates and returns stats for a Population pop"""
    sum_fitness = pop.sum_of_fitness
    pop_min = min(pop.fitness_lyst)
    pop_max = max(pop.fitness_lyst)
    pop_mean = pop.sum_of_fitness / pop.pop_size
    return sum_fitness, pop_min, pop_max, pop_mean

def report(pop: Population, gen_num: int):
    """Formats and prints observation information and summary statistics for
    each generation

    """
    print(f"Generation {gen_num}")
    print("-" * 100)

    sof, pmin, pmax, pmean = stats(pop)
    labels = f"Num  Genotype                         x/c      Fitness"
    print(labels)

    # Print individual statistics
    for indiv in pop.pop:
        print(indiv)
    print("-" * 100)

    # Print generation statistics
    report_str = f"Generation {gen_num} Cumulative Statistics    max: "\
                 f"{pmax:.4f}    min: {pmin:.4f}    mean: {pmean:.4f}"\
                 f"    sum: {sof:.4f}"
    print(report_str)
    print("=" * 100)

    max_index = where(pop.fitness_lyst == pmax)[0][0]
    top_individual = pop.pop[max_index]
    print(f"Top Individual                    x*            z*        fitness")
    print(f"{top_individual.genotype}{top_individual.phenotype:>14}"\
          f"    {top_individual.phenotype / top_individual.c:.4f}"\
          f"    {top_individual.fitness:.4f}")
    print("=" * 100)