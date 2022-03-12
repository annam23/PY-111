from typing import Hashable, List
import networkx as nx
from collections import deque


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """

    queue_nodes = deque()
    queue_nodes.append(start_node)

    result_nodes = []
    visited_nodes = {start_node}

    while queue_nodes:
        current_node = queue_nodes.popleft()
        neighbours = g[current_node]

        for neighbour in neighbours:
            if neighbour not in visited_nodes:
                queue_nodes.append(neighbour)
                visited_nodes.add(neighbour)

        result_nodes.append(current_node)

    print(result_nodes)
    return result_nodes
