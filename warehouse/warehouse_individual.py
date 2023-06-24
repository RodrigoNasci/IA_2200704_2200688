from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = []
        # TODO

    def compute_fitness(self) -> float:
        # TODO
        self.fitness = 0
        pairs = self.problem.agent_search.pairs.copy()
        for gene in self.genome:
            for i in range(len(gene)-1):
                cell = gene[i]
                next_cell = gene[i + 1]
                for pair in pairs:
                    if (cell.line == pair.cell1.line and cell.column == pair.cell1.column and next_cell.line == pair.cell2.line and next_cell.column == pair.cell2.column) or (cell.line == pair.cell2.line and cell.column == pair.cell2.column and next_cell.line == pair.cell1.line and next_cell.column == pair.cell1.column):
                        self.fitness += pair.value
        return self.fitness
    # calcular os caminhos comlpletos percorridos pelos froklifts. Devolve uma lista de listas (as celulas percorridas por cada forklift)
    # e o n max de passos necessarios para percorrer todos os caminhos (i.e, o n de celulas do caminho mais longo percorrido por um forklift)

    def obtain_all_path(self):
        # TODO
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        #string += str (self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance