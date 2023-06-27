from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation
from ga.genetic_algorithm import GeneticAlgorithm

class Mutation2(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        # swap mutation
        ind.num_genes = len(ind.genome)
        for i in range(ind.num_genes-1):
            if GeneticAlgorithm.rand.random() < self.probability:
                aux = ind.genome[i]
                ind.genome[i] = ind.genome[i+1]
                ind.genome[i+1] = aux

    def __str__(self):
        return "Mutation mutação de troca de genes adjacentes (" + f'{self.probability}' + ")"
