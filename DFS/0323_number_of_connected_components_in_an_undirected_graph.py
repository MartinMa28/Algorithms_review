class Graph:
    def __init__(self, v_num):
        self.v_num = v_num
        self.adj = [[] for _ in range(self.v_num)]

    def add_adj(self, x, y):
        """
        adds undirected edge between adjacent vertices
        """
        self.adj[x] = y
        self.adj[y] = x


class Solution:

    def countComponents_top_down(self, v_num, edge_l):
        """
        DFS following the pattern down below:
        1. push to stack
        2. pop the top of the stack, add it to visited
        3. retrieve all of unvisited neighbors of the popped top
        4. push unvisited neighbots to the stack
        5. go to 1, until the stack become empty
        """
        adj_list = [[] for _ in range(v_num)]

        # make the adjacent list for the graph
        for edge in edge_l:
            v_from = edge[0]
            v_to = edge[1]

            adj_list[v_from].append(v_to)
            adj_list[v_to].append(v_from)

        count = 0
        stack = []
        visited = []

        for i in range(v_num):
            if i not in visited:
                count += 1
                stack.append(i)

                while len(stack) > 0:
                    node = stack.pop()
                    visited.append(node)
                    neighbors = adj_list[node]

                    for neighbor in neighbors:
                        if neighbor not in visited:
                            stack.append(neighbor)

        return count


    # def countComponents_btm_up(self, v_num, edge_l):
    #     adj_list = [[] for _ in range(v_num)]

    #     for e in edge_l:
    #         v_from = e[0]
    #         v_to = e[1]

    #         adj_list[v_from].append(v_to)
    #         adj_list[v_to].append(v_from)

    #     stack = []
    #     visited = []
    #     count = 0

    #     for v in range(v_num):
    #         cur_v = v
    #         while 
        
    



if __name__ == "__main__":
    solu = Solution()
    edge_list = [[0, 1], [1, 2], [3, 4]]
    print(solu.countComponents_top_down(5, edge_list))