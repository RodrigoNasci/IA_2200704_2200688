import random

from ga.individual import Individual
from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual


class WarehouseProblemGA(Problem):
    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search

    def generate_individual(self) -> "WarehouseIndividual":
        # TODO
        warehouse = WarehouseIndividual(self, 0)
        for forkl in self.forklifts:
            gene = [forkl]
            produtosList = self.products.copy()
            random.shuffle(produtosList)
            for produto in produtosList:
                gene.append(produto)
            warehouse.genome.append(gene)

        return warehouse

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

