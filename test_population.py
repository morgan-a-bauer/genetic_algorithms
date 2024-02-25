"""
test_population.py
Morgan Bauer
22 February 2024

Tests for the population class in homework 01 for CS-470 Evolutionary
Computation
pledged
"""
from population import Population
from objective_funcs import objective_func_1, objective_func_2, objective_func_3
from numpy import array as nparray

def test_evaluate_fitness(pop: Population) -> None:
    """Tests the evaluate_fitness() method of the Population class to ensure
    accuracy of calculations

    """
    pop.evaluate_fitness()
    print(pop.selection_probs)
    print(pop.sum_of_fitness)

def test_select_parents(pop: Population, num_times: int) -> None:
    """Tests the select_parents() method of the Population class to ensure the
    distribution of parents chosen aligns with the expected distribution

    """
    probs = pop.selection_probs
    observed = nparray([0 for i in range(len(probs))], dtype = "float")

    for i in range(num_times):
        p1 = pop.select_parent()
        observed[p1] += 1.0
    observed /= num_times
    diffs = [abs(probs[i] - observed[i]) for i in range(len(probs))]
    print(diffs)

def test_new_generation(pop: Population) -> None:
    new_gen = pop.new_generation()
    print(new_gen)
    print(new_gen.pop)
    print("Length:", len(new_gen.pop))

if __name__ == "__main__":
    # Test initialization
    p1 = Population(100, [], 0.5, 0.01, 30, objective_func_1, 10)
    print(p1.pop)
    for i in p1.pop:
        print(i)

    p2 = Population(100, [], 0.5, 0.01, 30, objective_func_2, 0)
    print(p2.pop)
    for i in p2.pop:
        print(i)

    p3 = Population(100, [], 0.5, 0.01, 30, objective_func_3, 0)
    print(p3.pop)
    for i in p3.pop:
        print(i)

    # Test evaluate_fitness()
    print("=" * 100)
    print("Testing evaluate_fitness()\n")
    test_evaluate_fitness(p1)
    print()
    test_evaluate_fitness(p2)
    print()
    test_evaluate_fitness(p3)
    print("\nevaluate_fitness() tests complete")

    print("=" * 100)
    print("Testing select_parents()\n")
    test_select_parents(p1, 1000)
    print()
    test_select_parents(p2, 1000)
    print()
    test_select_parents(p3, 1000)
    print("select_parents() tests complete")

    print("=" * 100)
    print("Testing new_generation()\n")
    test_new_generation(p1)
    test_new_generation(p2)
    test_new_generation(p3)
    print("\nnew_generation() tests completed")