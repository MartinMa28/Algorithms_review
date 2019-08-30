class Solution:
    def __init__(self):
        self.results = []

    def _backtrack(self, left, right, cur_str) -> None:
        if left == 0 and right == 0:
            self.results.append(cur_str)
        elif left == right:
            self._backtrack(left - 1, right, cur_str + '(')
        else:
            if left > 0:
                self._backtrack(left - 1, right, cur_str + '(')
            self._backtrack(left, right -1, cur_str + ')')

    def generateParenthesis(self, n: int) -> list:
        self._backtrack(n, n, '')
        
        return self.results


if __name__ == "__main__":
    solu = Solution()
    print(solu.generateParenthesis(3))