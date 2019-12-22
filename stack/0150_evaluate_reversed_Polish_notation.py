class Solution:
    
    def evalRPN(self, tokens: list) -> int:
        operators = set(('+', '-', '*', '/'))
        stack = []
        
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                res = -1
                
                if t == '+':
                    res = left_operand + right_operand
                elif t == '-':
                    res = left_operand - right_operand
                elif t == '*':
                    res = left_operand * right_operand
                else:
                    if left_operand * right_operand > 0:
                        res = left_operand // right_operand
                    else:
                        res = -(abs(left_operand) // abs(right_operand))
                    
                stack.append(res)
                
                
        return stack[0]
                    