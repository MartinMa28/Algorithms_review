from collections import deque

class Solution:
        
    def findOrder(self, numCourses: int, prerq: list) -> list:
        # build an adjcaent list
        graph = {}
        
        for e in prerq:
            if e[1] in graph:
                graph[e[1]].append(e[0])
            else:
                graph[e[1]] = [e[0]]
        
        indegree = [0 for _ in range(numCourses)]
        
        for course in range(numCourses):
            if course in graph:
                for neighbor in graph[course]:
                    indegree[neighbor] += 1
                
        queue = deque()
        res = []
        # push all of nodes that has 0 in-degree
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while len(queue) > 0:
            popped = queue.popleft()
            res.append(popped)
            
            if popped in graph:
                for neighbor in graph[popped]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                        
        if len(res) < numCourses:
            return []
                    
        return res