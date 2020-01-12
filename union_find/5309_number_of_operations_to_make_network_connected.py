class DisjointSet:
    class Node:
        def __init__(self, x):
            self.parent = self
            self.rank = 0
            self.val = x
    
    def __init__(self, n):
        self.nodes = [DisjointSet.Node(i) for i in range(n)]
    
    def _find(self, node:'DisjointSet.Node') -> 'DisjointSet.Node':
        if node.parent is node:
            return node
        
        node.parent = self._find(node.parent)
        return node.parent
    
    def find(self, val: int) -> int:
        return self._find(self.nodes[val]).val
    
    def union(self, x: int, y: int) -> None:
        x_parent = self._find(self.nodes[x])
        y_parent = self._find(self.nodes[y])
        
        if x_parent is y_parent:
            return
        elif x_parent.rank > y_parent.rank:
            y_parent.parent = x_parent
        elif x_parent.rank < y_parent.rank:
            x_parent.parent = y_parent
        else:
            y_parent.parent = x_parent
            x_parent.rank += 1

class Solution:
    def makeConnected(self, n: int, connections: list) -> int:
        if len(connections) < n - 1:
            return -1
        
        disjoint_set = DisjointSet(n)
        for n1, n2 in connections:
            disjoint_set.union(n1, n2)
            
        root_set = set()
        
        for i in range(n):
            root_set.add(disjoint_set.find(i))
            
        return len(root_set) - 1