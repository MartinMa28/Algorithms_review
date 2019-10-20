import heapq

class Solution:
    def _help(self, slots1: list, slots2: list, duration: int) -> list:
        if slots1 == [] or slots2 == []:
            return []
        
        if slots1[0][1] < slots2[0][0] + duration:
            heapq.heappop(slots1)
            return self._help(slots1, slots2, duration)
        
        if slots2[0][1] < slots1[0][0] + duration:
            heapq.heappop(slots2)
            return self._help(slots1, slots2, duration)
        
        return [max((slots1[0][0], slots2[0][0])), max((slots1[0][0], slots2[0][0])) + duration]

    def minAvailableDuration(self, slots1: list, slots2: list, duration: int) -> list:
        heapq.heapify(slots1)
        heapq.heapify(slots2)
        return self._help(slots1, slots2, duration)


if __name__ == "__main__":
    solu = Solution()
    print(solu.minAvailableDuration([[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]],\
        [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]], 456085))