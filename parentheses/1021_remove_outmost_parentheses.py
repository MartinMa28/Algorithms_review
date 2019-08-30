from functools import reduce

class Solution:
    def removeOutermostParentheses(self, S: str) -> str:
        stack = []
        primi_splits = []

        for idx, s in enumerate(S):
            if s == '(':
                stack.append(idx)
            elif s == ')':
                start_idx = stack.pop()
                if len(stack) == 0:
                    primi_splits.append(S[start_idx: idx + 1])
        
        return str(reduce(lambda x, y: x + y, map(lambda x: x[1:-1], primi_splits)))


if __name__ == "__main__":
    solu = Solution()
    S = '(()())(())'
    print(solu.removeOutermostParentheses(S))
