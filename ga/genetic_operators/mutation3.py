from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        # Invert
        ind.num_genes = len(ind.genome)
        for i in range(ind.num_genes):
            j = (ind.num_genes-1)-i
            if i < j:
                if GeneticAlgorithm.rand.random() < self.probability:
                    aux = ind.genome[i]
                    ind.genome[i] = ind.genome[j]
                    ind.genome[j] = aux


    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
