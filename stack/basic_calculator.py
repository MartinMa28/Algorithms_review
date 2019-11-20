from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        # remove whitespace
        s = ''.join(filter(lambda ch: ch != ' ', s))
        
        idx = 0
        
        stack = []
        
        res = 0
        while idx < len(s):
            if s[idx] == '(' or s[idx] == '+' or s[idx] == '-':
                stack.append(s[idx])
                idx += 1
            elif s[idx].isnumeric():
                str_n = ''
                while idx < len(s) and s[idx].isnumeric():
                    str_n += s[idx]
                    idx += 1
                    
                stack.append(int(str_n))
            else:
                # closing parenthesis
                evaluate = []
                while len(stack) > 0 and stack[-1] != '(':
                    evaluate.append(stack.pop())
                    
                stack.pop()

                res = evaluate.pop()

                while len(evaluate) > 0:
                    popped = evaluate.pop()
                    if popped == '+':
                        right_op = evaluate.pop()
                        res += right_op
                    elif popped == '-':
                        right_op = evaluate.pop()
                        res -= right_op

                stack.append(res)
                idx += 1
        
        
        evaluate = deque(stack)

        res = evaluate.popleft()
        while len(evaluate) > 0:
            popped = evaluate.popleft()
            if popped == '+':
                right_op = evaluate.popleft()
                res += right_op
            elif popped == '-':
                right_op = evaluate.popleft()
                res -= right_op
                    
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.calculate("(1+(4+5+2)-3)+(6+8)"))