"""
individual.py
Morgan Bauer
22 February 2024

Homework 01 for CS-470 Evolutionary Computation
An individual class for the implementation of the Simple Genetic Algorithm (SGA)
in sga.py
pledged
"""
from util import mutation, crossover
from random import randrange

class Individual:
    def __init__(self, genotype: str, parent1: int, parent2: int, x_site: int,
                 pc: float, pm: float, c: int):
        self.__genotype = genotype  # A binary string
        self.__phenotype = int(genotype, 2)  # The integer representation of
                                             # the genotype
        self.__fitness = 0
        self.__parent1 = parent1  # Index of parent1
        self.__parent2 = parent2  # Index of parent2
        self.__x_site = x_site  # The site at which parent1 and parent2 crossed
        self.__pc = pc  # Probability of crossover
        self.__pm = pm  # Probability of mutation
        self.__c = c  # Normalization constant
        self.__pop_index = 0  # The individual's index within the population

    @property
    def genotype(self) -> str:
        return self.__genotype

    @property
    def phenotype(self) -> int:
        return self.__phenotype

    @property
    def fitness(self) -> float:
        return self.__fitness

    @property
    def parent1(self) -> int:
        return self.__parent1

    @property
    def parent2(self) -> int:
        return self.__parent2

    @property
    def x_site(self) -> int:
        return self.__x_site

    @property
    def pc(self) -> float:
        return self.__pc

    @property
    def pm(self) -> float:
        return self.__pm

    @property
    def pop_index(self) -> int:
        return self.__pop_index

    @pop_index.setter
    def pop_index(self, i: int) -> None:
        self.__pop_index = i

    @property
    def c(self) -> int:
        return self.__c

    def evaluate_fitness(self, func, c: int, n: int) -> float:
        """Evaluates the fitness of an individual by passing its phenotype
        into a given fitness function

        Input:
        func -- a function used to evaluate the individual's fitness
        c -- an integer normalization constant to convert the phenotype into a
             float in [0, 1]
        n -- an integer exponent

        """
        self.__fitness = func(self.__phenotype, c, n)
        return self.__fitness

    def mutate(self, mutation_pt: int) -> None:
        """Sometimes mutates one bit of the Individual's genotype at a randomly
        generated mutation point. Whether the bit is mutated or not depends on
        a choice from a Bernoulli distribution with pm being the probability of
        success (mutation)

        Input:
        mutation_pt -- the index at which a mutation may occur

        """
        self.__genotype = mutation(self.__genotype, mutation_pt,
                                   self.__pm)

    def __mul__(self, other) -> tuple:
        """Overloads the multiplication operator to perform a crossover between
        two members of the Individual class. Returns two child strings and a
        status indicating whether there was a crossover or not

        """
        crossover_pt = randrange(1, len(self.__genotype))

        child1, child2, crossed = crossover(self.__genotype, other.genotype,
                                            crossover_pt, self.__pc)

        # Initialize Individual objects for both children
        child1 = Individual(child1, self.__pop_index, other.pop_index,
                            crossover_pt, self.__pc, self.__pm, self.__c)
        child2 = Individual(child2, self.__pop_index, other.pop_index,
                            crossover_pt, self.__pc, self.__pm, self.__c)

        if crossed:  # Mutation may occur if the strings crossed
            for bit_pos in range(len(child1.genotype)):
                child1.mutate(bit_pos)
                child2.mutate(bit_pos)

        return child1, child2

    def __str__(self) -> str:
        """Returns a formatted string of important data about the individual to
        be displayed when print(individual) is called

        """
        indiv_str = f"{self.__pop_index +1:<5}{self.__genotype}"\
                    f"{self.__phenotype / self.__c:>9.4f}"\
                    f"{self.__fitness:>9.4f}"
        return indiv_str