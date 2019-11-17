class DisjointSet:
    
    class Node:
        def __init__(self, x):
            self.parent = self
            self.rank = 0
            self.val = x
    
    
    def __init__(self):
        self.map = {}
    
    
    def make_set(self, graph):
        """
        Args:
            graph: the adjacent list of the graph
        """
        for v in graph:
            self.map[v] = DisjointSet.Node(v)
        
            
    
    def _find(self, node: 'DisjointSet.Node') -> 'DisjointSet.Node':
        if node == node.parent:
            return node
        
        node.parent = self._find(node.parent)
        return node.parent
    
    def find(self, x):
        return self._find(self.map[x]).val
    
    
    def union(self, x, y):
        n_x = self.map[x]
        n_y = self.map[y]
        
        root_x = self._find(n_x)
        root_y = self._find(n_y)
        
        if root_x is root_y:
            # In the same set.
            return
        else:
            if root_x.rank == root_y.rank:
                root_x.rank += 1
                root_y.parent = root_x
            elif root_x.rank > root_y.rank:
                root_y.parent = root_x
            else:
                root_x.parent = root_y


def kruskal(graph: dict, edges: list) -> tuple:
    """
    Args:
        graph: the adjacent list of the graph
        edges: a list of edges in this format: (vertex_u, vertex_v, distance)

    Return:
        (mst, min_distance)
            mst: A list of the edges in the MST
            min_distance: the minimum distance
    """
    djs = DisjointSet()
    djs.make_set(graph)

    edges = sorted(edges, key=lambda e: e[2])

    mst = []
    min_dist = 0
    for e in edges:
        if not djs.find(e[0]) is djs.find(e[1]):
            djs.union(e[0], e[1])
            mst.append((e[0], e[1]))
            min_dist += e[2]


    return mst, min_dist


if __name__ == "__main__":
    edges = [('a', 'b', 4), ('b', 'c', 8), ('c', 'd', 7),
            ('d', 'e', 9), ('e', 'f', 10), ('d', 'f', 14),
            ('c', 'f', 4), ('i', 'c', 2), ('i', 'g', 6),
            ('g', 'f', 2), ('h', 'g', 1), ('h', 'i', 7),
            ('a', 'h', 8), ('b', 'h', 11)]
    graph = {}

    for e in edges:
        if e[0] in graph:
            graph[e[0]].append(e[1])
        else:
            graph[e[0]] = [e[1]]

        if e[1] in graph:
            graph[e[1]].append(e[0])
        else:
            graph[e[1]] = [e[0]]

    mst, min_dist = kruskal(graph, edges)
    print(mst)
    print(min_dist)

    

