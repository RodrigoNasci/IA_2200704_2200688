import random

from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination
from ga.genetic_algorithm import GeneticAlgorithm

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO

        #Order Crossover
        length = len(ind1.genome)
        indices = list(range(length))
        random.shuffle(indices)

        individual1 = [-1] * length
        individual2 = [-1] * length

        for i in range(length):
            index = indices[i]
            individual1[index] = ind1.genome[index]
            individual2[index] = ind2.genome[index]

        for i in range(length):
            if individual1[i] == -1:
                individual1[i] = ind2.genome[i]
            if individual2[i] == -1:
                individual2[i] = ind1.genome[i]

        return individual1, individual2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
