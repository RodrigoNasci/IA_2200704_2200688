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
        index = len(self.products) + len(self.forklifts)
        new_ind = WarehouseIndividual(self, index - 1)
        random_products = random.sample(range(len(self.products)), len(self.products))
        chunk_size = len(random_products) // len(self.forklifts)
        chunks = [random_products[i:i + chunk_size] for i in range(0, len(random_products), chunk_size)]
        new_ind.genome = []
        for i, chunk in enumerate(chunks):
            new_ind.genome.extend(chunk)
            if i < len(self.forklifts) - 1:
                new_ind.genome.append(index)
                index += 1

        return new_ind

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

