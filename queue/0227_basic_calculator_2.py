class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join(filter(lambda ch: ch != ' ', s))
        if s == '':
            return 0
        
        queue = []
        
        idx = 0
        
        while idx < len(s):
            if s[idx].isnumeric():
                str_n = ''

                while idx < len(s) and s[idx].isnumeric():
                    str_n += s[idx]
                    idx += 1
                    
                queue.append(int(str_n))

            elif s[idx] == '+' or s[idx] == '-':
                queue.append(s[idx])
                
                idx += 1
            elif s[idx] == '*' or s[idx] == '/':
                operator = s[idx]
                left_operand = queue.pop()
                
                idx += 1
                str_n = ''

                while idx < len(s) and s[idx].isnumeric():
                    str_n += s[idx]
                    idx += 1
                    
                right_operand = int(str_n)
                
                if operator == '*':
                    res = left_operand * right_operand
                else:
                    res = left_operand // right_operand
                
                queue.append(res)

            else:
                # whitespace
                idx += 1
        
        
        res = queue[0]
        idx = 0
        
        # left-fold or reduce
        while idx < len(queue):
            if queue[idx] == '+':
                right_operand = queue[idx + 1]
                res += right_operand
            elif queue[idx] == '-':
                right_operand = queue[idx + 1]
                res -= right_operand
                
            idx += 1
            
        return res