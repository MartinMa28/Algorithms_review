class UnionFind:
    
    class Node:
        def __init__(self, x):
            self.parent = self
            self.rank = 0
            self.val = x
    
    
    def __init__(self):
        self.num_to_node = {}
    
    
    def make_set_by_edges(self, edges):
        for e in edges:
            if e[0] not in self.num_to_node:
                self.num_to_node[e[0]] = UnionFind.Node(e[0])
                
            if e[1] not in self.num_to_node:
                self.num_to_node[e[1]] = UnionFind.Node(e[1])
            
    
    def _find(self, node: 'UnionFind.Node') -> 'UnionFind.Node':
        if node == node.parent:
            return node
        
        node.parent = self._find(node.parent)
        return node.parent
    
    def find(self, x: int) -> int:
        return self._find(self.num_to_node[x]).val
    
    
    def union(self, x: int, y: int):
        n_x = self.num_to_node[x]
        n_y = self.num_to_node[y]
        
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
            
            
class Solution:
    def findRedundantConnection(self, edges: list) -> list:
        uf = UnionFind()
        uf.make_set_by_edges(edges)
        
        for e in edges:
            root_1 = uf.find(e[0])
            root_2 = uf.find(e[1])
            
            if root_1 == root_2:
                return e
            
            uf.union(e[0], e[1])


if __name__ == "__main__":
    solu = Solution()
    print(solu.findRedundantConnection([[1,2],[1,3],[2,3]]))