class Solution:
    def _dfs(self, node, node_map):
        if node in node_map:
            return
        
        new_node = Node(node.val, [])
        node_map[node] = new_node
        

        for nei in node.neighbors:
            self._dfs(nei, node_map)
            if node_map[nei] not in new_node.neighbors:
                new_node.neighbors.append(node_map[nei])
            if new_node not in node_map[nei].neighbors:
                node_map[nei].neighbors.append(new_node)

        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_map = {}
        self._dfs(node, node_map)
        
        return node_map[node]