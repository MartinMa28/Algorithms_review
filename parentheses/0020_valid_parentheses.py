class Solution:
    def __init__(self):
        self.opens = ('(', '[', '{')
        self.closes = (')', ']', '}')
        self.open_to_close = dict(zip(self.opens, self.closes))

    
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in self.opens:
                stack.append(ch)
            if ch in self.closes:
                if len(stack) == 0:
                    return False
                else:
                    prev_open = stack.pop()
                    if ch != self.open_to_close[prev_open]:
                        return False
        
        if len(stack) > 0:
            return False

        return True