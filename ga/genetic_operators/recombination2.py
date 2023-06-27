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

        genome_filho1 = [-1] * length
        genome_filho2 = [-1] * length

        for i in range(length):
            index = indices[i]
            genome_filho1[index] = ind1.genome[index]
            genome_filho2[index] = ind2.genome[index]

        for i in range(length):
            if genome_filho1[i] == -1:
                genome_filho1[i] = ind2.genome[i]
            if genome_filho2[i] == -1:
                genome_filho2[i] = ind1.genome[i]

        return genome_filho1, genome_filho2

    def __str__(self):
        return "Recombination Crossover por Ordem (" + f'{self.probability}' + ")"
