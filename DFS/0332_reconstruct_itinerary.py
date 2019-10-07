import heapq

class Solution:
    def __init__(self):
        self.results = []
        self.from_to = {}

    def _dfs(self, itinerary, departure) -> bool:
        if len(itinerary) == self.tickets_len + 1:
            self.results = itinerary
            return True
        
        if departure in self.from_to:
            dests = self.from_to[departure]
        else:
            return False

        for d in dests:
            if not d[1]:
                d[1] = True
                itinerary.append(d[0])
                if not self._dfs(itinerary, departure=d[0]):
                    # backtracking
                    d[1] = False
                    itinerary.pop()
                else:
                    return True
            

    def findItinerary(self, tickets: list) -> list:
        tickets.sort()
        self.tickets_len = len(tickets)
        for t in tickets:
            if t[0] not in self.from_to:
                self.from_to[t[0]] = [[t[1], False]]
            else:
                self.from_to[t[0]].append([t[1], False])

        self._dfs(['JFK'], 'JFK')

        return self.results


if __name__ == "__main__":
    solu = Solution()
    test = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    solu.findItinerary(test)
