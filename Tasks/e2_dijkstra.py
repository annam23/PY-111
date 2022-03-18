from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    # Входные условия: список посещенных узлов, начальные стоимости
    visited_nodes = {node: False for node in g.nodes}
    costs = {node: float("inf") for node in g.nodes}
    current_node = starting_node
    costs[current_node] = 0

    while True:
        visited_nodes[current_node] = True

        # Обновляем стоимости до соседей
        for neighbours in g[current_node]:
            edge = g[current_node][neighbours]
            weight = edge['weight']
            costs[neighbours] = min(costs[neighbours], costs[current_node] + weight)

       # Выбираем новый текущий узел
        not_visited_total_costs = {node: cost for node, cost in costs.items() if not visited_nodes[node]}
        if not not_visited_total_costs:
            break
        current_node, _ = min(
            not_visited_total_costs.items(),
            key=lambda item: item[1]
        )

    return costs







