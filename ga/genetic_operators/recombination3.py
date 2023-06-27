import random

from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm
class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        #Edge Recombination
        length = len(ind1.genome)
        cycle_start = random.randint(0, length - 1)

        individual1 = [-1] * length
        individual2 = [-1] * length

        cycle_parent1 = True
        idx = cycle_start
        while True:
            if cycle_parent1:
                individual1[idx] = ind1.genome[idx]
                individual2[idx] = ind2.genome[idx]
            else:
                individual1[idx] = ind2.genome[idx]
                individual2[idx] = ind1.genome[idx]

            idx = ind1.genome.index(ind2.genome[idx])

            if idx == cycle_start:
                break

            cycle_parent1 = not cycle_parent1

        for i in range(length):
            if individual1[i] == -1:
                individual1[i] = ind2.genome[i]
            if individual2[i] == -1:
                individual2[i] = ind1.genome[i]

        return individual1, individual2

    def __str__(self):
        return "Recombination Ciclo de Edge (" + f'{self.probability}' + ")"