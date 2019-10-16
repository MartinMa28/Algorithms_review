class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if str == '':
            return 0
        
        stack = []
        amount = 0

        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                cur = stack[-1]

                if ch != cur:
                    stack.pop()

                    if len(stack) == 0:
                        amount += 1
                else:
                    stack.append(ch)

        return amount


if __name__ == "__main__":
    solu = Solution()
    print(solu.balancedStringSplit('RLLLLRLRRR'))