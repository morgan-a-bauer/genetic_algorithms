"""
test_individual.py
Morgan Bauer
22 February 2024

Tests for the individual class in homework 01 for CS-470 Evolutionary
Computation
pledged
"""
from individual import Individual
from objective_funcs import objective_func_1, objective_func_2, objective_func_3
from random import randint

def test_mutation(indiv: Individual, pm: float, num_tests: int) -> None:
    """Tests the mutate() method of the class Individual to ensure that the
    resulting child strings are correct (i.e. they were crossed over at the
    correct index) and that they occur at the proper frequency

    Inputs:
    indiv -- an Individual object
    pm -- a float representing the probability of mutation
    num_tests -- an int representing the number of times to call mutate()

    """
    num_mutations = 0
    for i in range(num_tests):
        original = indiv.genotype
        indiv.mutate(10)
        new = indiv.genotype
        if new != original:
            num_mutations += 1

    mutation_freq = num_mutations / num_tests
    print(f'mutation frequency: {mutation_freq:.2f}')

def test_crossover_frequency(ind1: Individual, ind2: Individual,
                             num_crosses: int) -> None:
    """Tests the method __mul__(), which performs a crossover in the class
    Individual to ensure that the crossover occurs with a frequency of about pc

    Inputs:
    ind1 -- a first Individual object
    ind2 -- a second Individual object
    num_crosses -- an int representing the number of times to call crossover()

    """
    cross_count = 0
    for i in range(num_crosses):
        child1, child2, crossed = ind1 * ind2
        if crossed:
            cross_count += 1

    cross_freq = cross_count / num_crosses
    print(f'Cross frequency: {cross_freq:.2f}')

if __name__ == "__main__":
    i1 = Individual('1' * 30, 5, 4, 3, 0.5, 0.01)
    i2 = Individual('0' * 30, 5, 4, 3, 0.5, 0.01)
    i3 = Individual('10' * 15, 5, 4, 3, 0.4, 0.01)
    i4 = Individual('1' * 30, 5, 4, 3, 0.7, 0.01)
    i5 = Individual('0' * 30, 5, 4, 3, 0.7, 0.01)
    i6 = Individual('1' * 30, 5, 4, 3, 1.0, 0.01)
    i7 = Individual('0' * 30, 5, 4, 3, 1.0, 0.01)
    i8 = Individual('1' * 30, 5, 4, 3, 0.0, 0.01)
    i9 = Individual('0' * 30, 5, 4, 3, 0.0, 0.01)
    i10 = Individual('1' * 30, 5, 4, 3, 0.35, 0.01)
    i11 = Individual('0' * 30, 5, 4, 3, 0.35, 0.01)

    # testing evaluate_fitness()
    print("=" * 100)
    print("Testing evaluate_fitness()")
    print("\ni1.evaluate_fitness(objective_func_1, 2 ** 30 - 1, 10)")
    print("Expected: 1.0")
    print("Observed:", i1.evaluate_fitness(objective_func_1, 2 ** 30 - 1, 10))
    print("\ni2.evaluate_fitness(objective_func_1, 2 ** 30 - 1, 10)")
    print("Expected: 0.0")
    print("Observed:", i2.evaluate_fitness(objective_func_1, 2 ** 30 - 1, 10))
    print("\ni3.evaluate_fitness(objective_func_1, 2 ** 30 - 1, 10)")
    print("Expected: 0.017341529915832606")
    print("Observed:", i3.evaluate_fitness(objective_func_1, 2 ** 30 - 1, 10))
    print("\ni1.evaluate_fitness(objective_func_2, 2 ** 30 - 1, 10)")
    print("Expected: 0.0")
    print("Observed:", i1.evaluate_fitness(objective_func_2, 2 ** 30 - 1, 10))
    print("\ni2.evaluate_fitness(objective_func_2, 2 ** 30 - 1, 10)")
    print("Expected: 0.0")
    print("Observed:", i2.evaluate_fitness(objective_func_2, 2 ** 30 - 1, 10))
    print("\ni3.evaluate_fitness(objective_func_2, 2 ** 30 - 1, 10)")
    print("Expected: 0.5514403292181065")
    print("Observed:", i3.evaluate_fitness(objective_func_2, 2 ** 30 - 1, 10))
    print("\ni1.evaluate_fitness(objective_func_3, 2 ** 30 - 1, 10)")
    print("Expected: 1.9899020385619612")
    print("Observed:", i1.evaluate_fitness(objective_func_3, 2 ** 30 - 1, 10))
    print("\ni2.evaluate_fitness(objective_func_3, 2 ** 30 - 1, 10)")
    print("Expected: 2.0")
    print("Observed:", i2.evaluate_fitness(objective_func_3, 2 ** 30 - 1, 10))
    print("\ni3.evaluate_fitness(objective_func_, 2 ** 30 - 1, 10)")
    print("Expected: 2.543712422917209")
    print("Observed:", i3.evaluate_fitness(objective_func_3, 2 ** 30 - 1, 10))
    print("\nevaluate_fitness() test completed")

    # testing mutation()
    # mutation frequency should approxmiate pm
    print("=" * 100)
    print("Testing mutate()")
    print("Testing mutate with pm = 0.5 and i1")
    test_mutation(i1, 0.5, 1000)
    print("Testing mutate with pm = 0.7 and i2")
    test_mutation(i2, 0.7, 1000)
    print("Testing mutate with pm = 1.0 and i3")
    test_mutation(i3, 1.0, 1000)
    print("Testing mutate with pm = 0.0 and i1")
    test_mutation(i1, 0.0, 1000)
    print("Testing mutate with pm = 0.35 and i2")
    test_mutation(i2, 0.35, 1000)
    print("mutate() tests complete")

    # testing __mul__() or crossover
    #crossover frequency should be about pc
    print("=" * 100)
    print("Testing __mul__()")
    print("\nTesting frequency of crossover")
    print("Testing crossover with pc = 0.5 and string length 30")
    test_crossover_frequency(i1, i2, 1000)
    print("Testing crossover with pc = 0.7 and string length 30")
    test_crossover_frequency(i4, i5, 1000)
    print("Testing crossover with pc = 1.0 and string length 30")
    test_crossover_frequency(i6, i7, 1000)
    print("Testing crossover with pc = 0.0 and string length 30")
    test_crossover_frequency(i8, i9, 1000)
    print("Testing crossover with pc = 0.35 and string length 30")
    test_crossover_frequency(i10, i11, 1000)

    # This part will not be accurate, this test was run with a set crossover
    # point and a pc of 1.0
    i12 = Individual('1' * 30, 5, 4, 3, 0.5, 0.01)
    i13 = Individual('0' * 30, 5, 4, 3, 0.5, 0.01)
    print("\nTesting accuracy of crossover")
    child1, child2, crossed = i12 * i13
    print("Expected:", "1" * 15 + "0" * 15)
    print("Observed:", child1.genotype)
    print("Expected:", "0" * 15 + "1" * 15)
    print("Observed:", child2.genotype)
    print("__mul__() tests complete")

    # Testing __str__()
    print("=" * 100)
    print("Testing __str__()")
    indiv_lyst = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13]
    for indiv in indiv_lyst:
        print(indiv)
    print("__str__() tests complete")