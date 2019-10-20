from itertools import combinations

class Solution:
    def __init__(self):
        self.combs = []

    def _dfs(self, cur_num, cur_comb, n, k):
        if k - len(cur_comb) > n - cur_num + 1:
            return
        else:
            if len(cur_comb) == k:
                if cur_comb not in self.combs:
                    self.combs.append(cur_comb.copy())
            else:
                for num in range(cur_num + 1, n + 1):
                    cur_comb.append(num)
                    self._dfs(num, cur_comb, n, k)
                    # backtracking
                    cur_comb.pop()
    
    def probabilityOfHeads(self, prob: list, target: int) -> float:
        combs = [set(c) for c in combinations(range(len(prob)), target)]
        all_coins = set(range(len(prob)))
        probability = 0

        for c in combs:
            cur_prob = 1
            for i in c:
                cur_prob *= prob[i]

            for i in all_coins - c:
                cur_prob *= (1 - prob[i])

            probability += cur_prob

        return probability
        

        

if __name__ == "__main__":
    solu = Solution()
    print(solu.probabilityOfHeads([0,0,0,0,0], 5))