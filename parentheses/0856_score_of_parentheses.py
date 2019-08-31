from functools import reduce

class Solution:
    def __init__(self):
        self.score = 0

    def _primitive_split(self, s: str) -> list:
        stack = []
        primitives = []
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
            else:
                prev_open = stack.pop()
                if len(stack) == 0:
                    primitives.append(s[prev_open: idx + 1])
        
        return primitives    
                

    def scoreOfParentheses(self, S: str) -> int:
        # split the whole string into primitive parentheses
        if S == '()':
            return 1
        else:
            primitives = self._primitive_split(S)
            if len(primitives) == 1:
                if len(primitives[0]) > 2:
                    self.score = 2 * self.scoreOfParentheses(primitives[0][1: -1])
            else:
                self.score = sum(map(self.scoreOfParentheses, primitives))

        return self.score

    
    


if __name__ == "__main__":
    solu = Solution()
    print(solu.scoreOfParentheses("(()(()))"))
