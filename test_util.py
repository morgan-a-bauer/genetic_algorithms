"""
test_util.py
Morgan Bauer
08 February 2024

Tests for homework 00 for CS-470 Evolutionary Computation
pledged
"""

import matplotlib.pyplot as plt
import numpy as np
import util
from random import randint

def test_pseudorandom_integer(lower_bound: int, upper_bound: int,
                              num_ints: int) -> None:
    """Tests the function pseudorandom_integer() in util.py to ensure
    that the distribution is near uniform.

    Inputs:
    lower_bound -- the lower bound for the range the integer may be in
    upper-bound -- the upper bound for the range the integer may be in
    num_ints -- the number of integers to generate for testing

    """
    int_array = np.zeros(shape = num_ints, dtype = int)

    for i in range(num_ints):
        m = util.pseudorandom_integer(lower_bound, upper_bound)
        int_array[i] = m

    plt.hist(int_array)
    plt.show()

def test_crossover(parent1: str, parent2: str, crossing_points: list,
                   pc: float) -> None:
    """Tests the function crossover() in util.py to ensure that the
    resulting child strings are correct (i.e. they were crossed over at the
    correct index)

    Inputs:
    parent1 -- the first parent string (a binary string)
    parent2 -- the second parent string (a binary string)
    crossing_points -- a list of indeces at which the parent strings should be
                       crossed
    pc -- a float representing the probability of crossover

    """
    for cp in crossing_points:
        print(f'Crossing point: {cp}')
        child1, child2 = util.crossover(parent1, parent2, cp, pc)
        print(f'child1: {child1}')
        print(f'child2: {child2}')

def test_crossover_frequency(pc: float, num_crosses: int, str_len: int) -> None:
    """Tests the function crossover() in util.py to ensure that the
    crossover occurs with a frequency of about pc

    Inputs:
    pc -- a float representing the probability of crossover
    num_crosses -- an int representing the number of times to call crossover()
    str_len -- an integer number of strings to be generated

    """
    cross_count = 0
    for i in range(num_crosses):
        parent1 = ''.join([str(randint(0, 1)) for j in range(str_len)])
        parent2 = ''.join([str(randint(0, 1)) for j in range(str_len)])
        ind = randint(0, str_len - 1)
        child1, child2 = util.crossover(parent1, parent2, ind, pc)
        if child1 != parent1 and child2 != parent2\
                             and parent1[ind:] != parent2[ind:]:
            cross_count += 1

    cross_freq = cross_count / num_crosses
    print(f'cross frequency: {cross_freq:.2f}')

def test_mutation(pm: float, num_tests: int, str_len: int) -> None:
    """Tests the function mutation() in util.py to ensure that the
    resulting child strings are correct (i.e. they were crossed over at the
    correct index) and that they occur at the proper frequency

    Inputs:
    pm -- a float representing the probability of mutation
    num_tests -- an int representing the number of times to call mutation()
    str_len -- an int length of binary strings to be generated

    """
    num_mutations = 0
    for i in range(num_tests):
        my_str = ''.join([str(randint(0, 1)) for j in range(str_len)])
        index = randint(0, str_len - 1)
        new_str = util.mutation(my_str, index, pm)
        if my_str != new_str:
            num_mutations += 1

    mutation_freq = num_mutations / num_tests
    print(f'mutation frequency: {mutation_freq:.2f}')


if __name__ == "__main__":
    # testing pseudorandom_integer()
    # should generate a near-uniform distribution
    print("=" * 100)
    print("Testing pseudorandom_integer()")
    test_pseudorandom_integer(3, 12, 1000)
    print("pseudorandom_integer() tests complete")

    # testing crossover()
    print("=" * 100)
    print("Testing crossover()")
    parent1 = '1011101011'
    parent2 = '0000110100'
    crossing_points = [-3, 1, 6, 20, 3.5, 'h', True, None]
    print("Expected Output:")
    print('Crossing point: -3')
    print('USAGE: Index out of range')
    print('Please enter a new crossing point: ')
    print('Crossing point: 1')
    print('child1: 0011101011')
    print('child2: 1000110100')
    print('Crossing point: 6')
    print('child1: 1011100100')
    print('child2: 0000111011')
    print('Crossing point: 20')
    print('USAGE: Index out of range')
    print('Please enter a new crossing point: ')
    print('Crossing point: 3.5')
    print('USAGE: crossing_point must be an integer')
    print('Please enter a new crossing point: ')
    print('Crossing point: "h"')
    print('USAGE: crossing_point must be an integer')
    print('Please enter a new crossing point: ')
    print('Crossing point: True')
    print('USAGE: crossing_point must be an integer')
    print('Please enter a new crossing point: ')
    print('Crossing point: None')
    print('USAGE: crossing_point must be an integer')
    print('Please enter a new crossing point: ')
    test_crossover(parent1, parent2, crossing_points, 1.0)
    parent3 = '0101'
    crossing_points2 = [4]
    print("USAGE: Parent strings do not have the same length")
    print("Please enter a new first parent: ")
    print("Please enter a new second parent: ")
    test_crossover(parent1, parent3, crossing_points2, 1.0)
    print("\nTesting frequency of crossover")
    print("Testing crossover with pc = 0.5 and string length 30")
    test_crossover_frequency(0.5, 1000, 30)
    print("Testing crossover with pc = 0.7 and string length 30")
    test_crossover_frequency(0.7, 1000, 30)
    print("Testing crossover with pc = 1.0 and string length 30")
    test_crossover_frequency(1.0, 1000, 30)
    print("Testing crossover with pc = 0.0 and string length 30")
    test_crossover_frequency(0.0, 1000, 30)
    print("Testing crossover with pc = 0.35 and string length 30")
    test_crossover_frequency(0.35, 1000, 30)
    print("crossover() tests complete")

    # testing mutation()
    # mutation frequency should approxmiate pm
    print("=" * 100)
    print("Testing mutation()")
    print("Testing mutation with pm = 0.5 and string length 5")
    test_mutation(0.5, 1000, 5)
    print("Testing mutation with pm = 0.7 and string length 12")
    test_mutation(0.7, 1000, 12)
    print("Testing mutation with pm = 1.0 and string length 3")
    test_mutation(1.0, 1000, 3)
    print("Testing mutation with pm = 0.0 and string length 3")
    test_mutation(0.0, 1000, 3)
    print("Testing mutation with pm = 0.35 and string length 47")
    test_mutation(0.35, 1000, 47)
    print("mutation() tests complete")