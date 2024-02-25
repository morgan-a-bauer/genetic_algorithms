"""
population.py
Morgan Bauer
22 February 2024

Homework 01 for CS-470 Evolutionary Computation
A population class for the implementation of the Simple Genetic Algorithm (SGA)
in sga.py
pledged
"""
from numpy import array as nparray
from random import randint, random
from individual import Individual

class Population:
    def __init__(self, pop_size: int, pop: list, pc: float, pm: float,
                 indiv_len: int, objective_func, n: int):
        self.__pop_size = pop_size
        self.__pop = pop  # List of Individual objects
        self.__pc = pc  # Probability of crossover
        self.__pm = pm  # Probability of mutation
        self.__indiv_len = indiv_len
        self.__sum_of_fitness = 0.0
        self.__fitness_lyst = nparray([0.0 for i in range(pop_size)])  # Array of floats
        self.__selection_probs = nparray([0.0 for i in range(pop_size)])  # Array of floats
        self.__objective_func = objective_func  # The objective function
        self.__c = 2 ** indiv_len - 1
        self.__n = n  # An exponent, only used for certain objective functions

        if pop == []:
            self.initialize()  # Creates the first generation randomly

    # Getters and setters
    @property
    def pop_size(self) -> int:
        return self.__pop_size

    @property
    def pop(self) -> list:
        return self.__pop

    @property
    def pc(self) -> float:
        return self.__pc

    @property
    def pm(self) -> float:
        return self.__pm

    @property
    def indiv_len(self) -> int:
        return self.__indiv_len

    @property
    def sum_of_fitness(self) -> float:
        return self.__sum_of_fitness

    @property
    def fitness_lyst(self) -> nparray:
        return self.__fitness_lyst

    @property
    def selection_probs(self) -> nparray:
        return self.__selection_probs

    @property
    def objective_func(self):
        return self.__objective_func

    @property
    def c(self) -> int:
        return self.__c

    @property
    def n(self) -> int:
        return self.__n

    def initialize(self) -> None:
        """If the population list provided to the constructor is empty,
        initialize() is called to populate the population list with Individual
        objects possessing randomly generated genotypes

        """
        for i in range(self.__pop_size):
            new_genotype = ''.join([str(randint(0, 1)) for i in range(30)])
            new_indiv = Individual(new_genotype, -1, -1, 0, self.__pc,
                                   self.__pm, self.__c)
            new_indiv.evaluate_fitness(self.__objective_func, self.__c,
                                       self.__n)
            self.__pop.append(new_indiv)
            new_indiv.pop_index = i

    def evaluate_fitness(self) -> None:
        """Loops through the list of individuals in the population, calculates
        their fitness, updates the sum of fitness, and places that fitness at
        the index of the selection probabilities list corresponding to the of
        the individual in the population list. Then divides all elements of the
        selection probabilities list by the sum of fitness

        """
        for pos, indiv in enumerate(self.__pop):
            indiv_fit = indiv.fitness
            self.__sum_of_fitness += indiv_fit
            self.__fitness_lyst[pos] = indiv_fit

        self.__selection_probs = self.__fitness_lyst / self.sum_of_fitness

    def select_parent(self) -> tuple:
        """Selects a random parent based on the Roullete Wheel algorithm"""
        partial_sum = 0
        rand = random() * self.__sum_of_fitness
        j = 0

        while partial_sum < rand and j != self.__pop_size - 1:
            j += 1
            partial_sum += self.__pop[j].fitness

        return j

    def new_generation(self):
        """Uses select, crossover, and mutation procedures to create a new
        generation

        """
        new_pop = []
        i = 0

        while len(new_pop) != self.__pop_size:
            # Get parents
            p1 = self.select_parent()
            p2 = self.select_parent()

            parent1 = self.__pop[p1]
            parent2 = self.__pop[p2]

            # Crossover using multiplication operator
            child1, child2 = parent1 * parent2

            child1.evaluate_fitness(self.__objective_func, self.__c, self.__n)
            child2.evaluate_fitness(self.__objective_func, self.__c, self.__n)

            # Set pop_index for individuals and increment index
            child1.pop_index = i
            new_pop.append(child1)
            i += 1
            child2.pop_index = i
            new_pop.append(child2)
            i += 1

        return Population(self.__pop_size, new_pop, self.__pc, self.__pm,
                          self.__indiv_len, self.__objective_func, self.__n)