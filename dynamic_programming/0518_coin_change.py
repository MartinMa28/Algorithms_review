class Solution:
    def __init__(self):
        self.res = set()


    def _dfs(self, amount: int, coins: list, cur_sum=[]) -> None:
        for c in coins:
            if cur_sum == [] or cur_sum[-1] <= c:
                cur_sum.append(c)
                if sum(cur_sum) == amount:
                    self.res.add(tuple(cur_sum))
                elif sum(cur_sum) < amount:
                    self._dfs(amount, coins, cur_sum)

                # backtracking when the sum exceeds the total amount
                cur_sum.pop()


    def change_recursive(self, amount: int, coins: list) -> int:
        if amount == 0:
            return 1

        self._dfs(amount, coins)
        res = len(self.res)
        self.res.clear()

        return res

    
    def change_slower(self, amount: int, coins: list) -> int:
        m = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        m[0][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                for k in range(j, -1, -coins[i - 1]):
                    m[i][j] += m[i - 1][k]

        return m[len(coins)][amount]

    
    def change(self, amount: int, coins: list) -> int:
        m = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        m[0][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                if j >= coins[i - 1]:
                    m[i][j] = m[i - 1][j] + m[i][j - coins[i - 1]]
                else:
                    m[i][j] = m[i - 1][j]

        return m[len(coins)][amount]
        

if __name__ == "__main__":
    coins = [1, 2]

    solu = Solution()
    print(solu.change(5000, coins))