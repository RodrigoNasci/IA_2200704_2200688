import random

from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm
class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        #Cycle Crossover
        length = len(ind1.genome)
        cycle_start = random.randint(0, length - 1)

        genome_filho1 = [-1] * length
        genome_filho2 = [-1] * length

        cycle_parent1 = True
        idx = cycle_start
        while True:
            if cycle_parent1:
                genome_filho1[idx] = ind1.genome[idx]
                genome_filho2[idx] = ind2.genome[idx]
            else:
                genome_filho1[idx] = ind2.genome[idx]
                genome_filho2[idx] = ind1.genome[idx]

            idx = ind1.genome.index(ind2.genome[idx])

            if idx == cycle_start:
                break

            cycle_parent1 = not cycle_parent1

        for i in range(length):
            if genome_filho1[i] == -1:
                genome_filho1[i] = ind2.genome[i]
            if genome_filho2[i] == -1:
                genome_filho2[i] = ind1.genome[i]

        return genome_filho1, genome_filho2

    def __str__(self):
        return "Recombination Crossover de Ciclo (" + f'{self.probability}' + ")"