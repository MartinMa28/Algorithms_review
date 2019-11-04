class Solution:
    def shortestDistance(self, words: list, word1: str, word2: str) -> int:
        i = -float('inf')
        j = -float('inf')
        dist = float('inf')

        for idx, w in enumerate(words):
            if w == word1:
                i = idx
            elif w == word2:
                j = idx

            if i >= 0 and j >= 0 and abs(i - j) < dist:
                dist = abs(i - j)

        return dist
        
        


if __name__ == "__main__":
    solu = Solution()
    print(solu.shortestDistance(["a","c","b","b","a"], "a", "b"))