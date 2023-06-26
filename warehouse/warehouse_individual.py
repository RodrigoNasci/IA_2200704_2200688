import copy

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

        for i in range(len(paths)):
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
                        if (forklift == pair.cell1 and product == pair.cell2) or (forklift == pair.cell2 and products == pair.cell1):
                            self.fitness += pair.value
                            break
                last = product
            for pair in pairs:
                if (last == pair.cell1 and self.exit == pair.cell2) or (last == pair.cell2 and self.exit == pair.cell1):
                    self.fitness += pair.value

        for i in range(len(paths)):
            if not paths[i]:
                self.fitness += 100

        self.steps = steps
        return self.fitness

    def obtain_all_path(self):
        # TODO
        paths = []
        products = self.problem.agent_search.products
        forklifts = self.problem.agent_search.forklifts
        aux = None
        steps = 1

        for i, value in enumerate(self.genome):
            if value >= len(products) + len(forklifts):
                if aux is None:
                    paths.append(self.genome[:i])
                    aux = i
                else:
                    paths.append(self.genome[aux+1:i])
                    aux = i
                steps += 1
            steps += 1
        if aux is not None:
            paths.append(self.genome[aux + 1:])
            steps += 1

        if len(forklifts) == 1:
            paths.append(self.genome)
            steps += 1
        return paths, steps

    def transformProduts(self, paths):
        products = self.problem.agent_search.products
        product_list = []
        for i in range(len(paths)):
            auxprodut = []
            for j in range(len(paths[i])):
                product = products[paths[i][j]]
                auxprodut.append(product)
            product_list.append(auxprodut)
        return product_list

    def __str__(self):
        genome_com_valor_produto_correto = []
        genome_com_seperar_forklift = []
        gene_forklift = []
        for gene in self.genome:
            if gene < len(self.problem.agent_search.products) + len(self.problem.agent_search.forklifts):
                genecorreto = copy.copy(gene)
                genecorreto += 1
                genome_com_valor_produto_correto.append(genecorreto)
                gene_forklift.append(genecorreto)
            else:
                genome_com_valor_produto_correto.append(gene)
                genome_com_seperar_forklift.append(gene_forklift)
                gene_forklift = []
        if gene_forklift != []:
            genome_com_seperar_forklift.append(gene_forklift)
        if len(self.problem.agent_search.forklifts) == 1:
            genome_com_seperar_forklift.append(genome_com_valor_produto_correto)

        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (genome_com_valor_produto_correto) + "\n\n"
        string += 'Numero de forklifts: ' + str(len(self.problem.agent_search.forklifts)) + "\n"
        if len(self.problem.agent_search.forklifts) != 1:
            string += 'Produtos capturados por forklift:\n'
            for i in range(len(self.problem.agent_search.forklifts)):
                string += 'forklift '+ str(i+1) + ': ' + str(genome_com_seperar_forklift[i]) + "\n"
        else:
            string += 'Produtos capturados pelo forklift 1:\n' + str(genome_com_seperar_forklift[0]) + "\n"

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