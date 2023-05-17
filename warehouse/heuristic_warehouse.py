from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        # TODO
        return abs(state.line_forklift - self._problem.goal_position.line) + abs(state.column_forklift - self._problem.goal_position.column)
        # para calcular a distancia em relação ao goal tem de ser apartir do line e colum fortklift
        """
        self.problem.goal_position
        """
        # pass
    def __str__(self):
        return "Distance between pairs"             # TODO

