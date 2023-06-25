from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.fitness = 0
        self.steps = 0
        self.exit = problem.agent_search.exit
        # TODO

    def compute_fitness(self) -> float:
        # TODO
        products = self.problem.agent_search.products
        forklifts = self.problem.agent_search.forklifts
        paths, steps = self.obtain_all_path()
        self.fitness = 0
        pairs = self.problem.agent_search.pairs.copy()
        last = None

        for i in range(len(paths)-1):
            if len(forklifts) == 1:
                forklift = forklifts[0]
            else:
                forklift = forklifts[i]
            aux= -1
            for j in range(len(paths[i])):
                product = products[paths[i][j]]
                if i == aux:
                    for pair in pairs:
                        if (last == pair.cell1 and product == pair.cell2) or (last == pair.cell2 and product == pair.cell1):
                            self.fitness += pair.value
                            break
                else:
                    aux = i
                    for pair in pairs:
                        if (forklift == pair.cell1 and product == pair.cell2) or (forklift == pair.cell2 and produc == pair.cell1):
                            self.fitness += pair.value
                            break
                last = product
            for pair in pairs:
                if (last == pair.cell1 and self.exit == pair.cell2) or (last == pair.cell2 and self.exit == pair.cell1):
                    self.fitness += pair.value

        for i in range(len(paths)):
            if not paths[i]:
                self.fitness += 100
        return self.fitness

    def obtain_all_path(self):
        # TODO
        paths = []
        products = self.problem.agent_search.products
        forklifts = self.problem.agent_search.forklifts
        aux = None
        steps = 0

        for i, value in enumerate(self.genome):
            if value >= len(products) + len(forklifts):
                if aux is None:
                    paths.append(self.genome[:i])
                    aux = i
                else:
                    paths.append(self.genome[aux+1:i])
                    aux = i
                steps += 1
        if aux is not None:
            paths.append(self.genome[aux + 1:])

        return paths, steps


    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
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