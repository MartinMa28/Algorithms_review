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

    def calculate_concise(self, s: str) -> int:
        s = ''.join(filter(lambda ch: ch != ' ', s))
        queue = deque()
        
        left = 0
        right = 0
        operators = {}
        operators['+'] = lambda a, b: a + b
        operators['-'] = lambda a, b: a - b
        operators['*'] = lambda a, b: a * b
        operators['/'] = lambda a, b: a // b
        
        while left < len(s) and right < len(s):
            while right < len(s) and s[right] not in ('+', '-', '*', '/'):
                right += 1
            
            queue.append(int(s[left:right]))
            
            if right < len(s):
                queue.append(s[right])

            left = right + 1
            right = right + 1
        
        sec_queue = deque([queue.popleft()])
        
        while queue:
            if queue[0] in ('+', '-'):
                sec_queue.append(queue.popleft())
                sec_queue.append(queue.popleft())
            else:
                # evaluate '/' and '*'
                operator = queue.popleft()
                right_op = queue.popleft()
                left_op = sec_queue[-1]
                
                evaluated = operators[operator](left_op, right_op)
                sec_queue[-1] = evaluated
                
        res = sec_queue.popleft()
        
        while sec_queue:
            operator = sec_queue.popleft()
            right_op = sec_queue.popleft()
            left_op = res
            
            evaluated = operators[operator](left_op, right_op)
            res = evaluated
            
        return res