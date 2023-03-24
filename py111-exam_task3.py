import networkx as nx


def connect_comp(g: nx.Graph):
    nodes = set(g.nodes())
    n = 0

    while nodes:
        start = nodes.pop()
        queue = [start, ]
        viewed = [start, ]
        res = set()
        while len(queue):
            n = queue.pop()
            res.add(n)
            for neighbor in g.neighbors(n):
                if neighbor not in viewed:
                    queue.append(neighbor)
                    viewed.append(neighbor)
                    nodes -= res
                    n += 1

            return n


