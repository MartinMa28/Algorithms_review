class Solution:
    def _dfs(self, idx, visited, tmp, indices, s, graph):
        if idx in visited:
            return
        
        visited.add(idx)
        tmp.append(s[idx])
        indices.append(idx)
        if idx in graph:
            for i in graph[idx]:
                self._dfs(i, visited, tmp, indices, s, graph)



    def smallestStringWithSwaps(self, s: str, pairs: list) -> str:
        graph = {}
        indices = []
        tmp = []
        visited = set()
        s = list(s)


        # build the undirected graph
        for p in pairs:
            if p[0] not in graph:
                graph[p[0]] = [p[1]]
            else:
                graph[p[0]].append(p[1])

            if p[1] not in graph:
                graph[p[1]] = [p[0]]
            else:
                graph[p[1]].append(p[0])

        for i in range(len(s)):
            if i in visited:
                continue

            self._dfs(i, visited, tmp, indices, s, graph)
            sorted_chars = sorted(tmp)
            sorted_indices = sorted(indices)

            for si, ch in enumerate(sorted_chars):
                s[sorted_indices[si]] = ch
                

            indices = []
            tmp = []

            

        min_s = ''
        for ch in s:
            min_s += ch

        return min_s

if __name__ == "__main__":
    solu = Solution()
    print(solu.smallestStringWithSwaps("udyyek", 
    [[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]]))


