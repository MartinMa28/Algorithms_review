class Solution:
    def __init__(self):
        self.res = []

    def _backtrack(self, left: int, right: int, cur: str) -> None:
        if left == 0 and right == 0:
            self.res.append(cur)
        elif left == right:
            self._backtrack(left - 1, right, cur + '(')
        elif left > 0:
            self._backtrack(left - 1, right, cur + '(')
            self._backtrack(left, right - 1, cur + ')')
        else:
            self._backtrack(left, right - 1, cur + ')')

    def generateParenthesis(self, n: int) -> list:
        self._backtrack(n, n, '')
        res = self.res
        self.res = []
        
        return res