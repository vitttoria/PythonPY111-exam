import networkx as nx


def connect_graph(g: nx.Graph):
    nodes = set(g.nodes())
    number = 0

    while nodes:
        start = nodes.pop()
        queue = [start, ]
        viewed = [start, ]
        result = set()
        while len(queue):
            number = queue.pop()
            result.add(number)
            for neighbor in g.neighbors(number):
                if neighbor not in viewed:
                    queue.append(neighbor)
                    viewed.append(neighbor)
                    nodes -= result
                    number += 1

            return number

