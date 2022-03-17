from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    #Входные условия: список посещенных узлов, начальные стоимости
    visited_nodes = {node: False for node in g}
    costs = {node: float("inf") for node in g}
    costs[starting_node] = 0

    while visited_nodes is not True:
        visited_nodes[starting_node] = True
        neighbours = g[starting_node]
        cost = costs[visited_nodes]
        for n in neighbours.keys():
             new_cost = cost + neighbours[n]
             if costs[n] > new_cost:





