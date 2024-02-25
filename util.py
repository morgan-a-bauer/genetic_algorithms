"""
util.py
Morgan Bauer
08 February 2024

Homework 00 for CS-470 Evolutionary Computation
pledged
"""

from random import randint
from scipy.stats import bernoulli

def pseudorandom_integer(lower_bound: int, upper_bound: int) -> int:
    """Returns a pseudorandom integer in a given range

    Input:
    lower_bound -- the lower bound of the range
    upper_bound -- the upper_bound of the range

    """
    m = randint(lower_bound, upper_bound)

    return m

def crossover(parent1: str, parent2: str, crossing_point: int,
              pc: float) -> tuple:
    """Returns a tuple containing the two child strings resulting from the
    crossover of parent1 and parent2

    Input:
    parent1 -- the first parent string
    parent2 -- the second parent string
    crossing_point -- the index at which the two parent strings are crossed
    pc -- a float representing the probability of a crossover occuring

    """
    while True:
        try:
            if len(parent1) != len(parent2):
                raise RuntimeError

            if crossing_point > len(parent1) or crossing_point < 0:
                raise IndexError

            child1 = parent1
            child2 = parent2

            cross = bernoulli.rvs(pc, size = 1)[0]

            if cross:
                child1 = parent1[:crossing_point] + parent2[crossing_point:]
                child2 = parent2[:crossing_point] + parent1[crossing_point:]

            return (child1, child2, cross)

        except RuntimeError:
            parent1 = 7
            parent2 = 3

            while type(parent1) != str or type(parent2) != str:
                print("USAGE: Parent strings do not have the same length")
                parent1 = input("Please enter a new first parent: ")
                parent2 = input("Please enter a new second parent: ")

        except TypeError:
            print("USAGE: crossing_point must be an integer")
            crossing_point = int(input("Please enter a new crossing point: "))

        except IndexError:
            print("USAGE: Index out of range")
            crossing_point = int(input("Please enter a new crossing point: "))

def mutation(s: str, mutation_point: int, pm: float) -> str:
    """Takes a binary string and mutates it at mutation_point with probability
    pm

    Input:
    s -- the binary string to be mutated
    mutation_point -- the index at which s will be mutated
    pm -- the probability of mutation

    """
    mutate = bernoulli.rvs(pm, size = 1)[0]

    s_prime = s

    if mutate:
        s_prime = s[:mutation_point] + str(int(not(int(s[mutation_point]))))\
            + s[mutation_point +1:]

    return s_prime