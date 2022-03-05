from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    stack_nodes = list()
    stack_nodes.append(start_node)

    result_nodes = []
    visited_nodes = {start_node}

    while stack_nodes:
        current_node = stack_nodes.pop()

        for neighbour in g[current_node]:
            if neighbour not in visited_nodes:
                stack_nodes.append(neighbour)
                visited_nodes.add(neighbour)

        result_nodes.append(current_node)

    return result_nodes
