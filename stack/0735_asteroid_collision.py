class Solution:
    def asteroidCollision(self, asteroids: list) -> list:
        positive_stack = []
        res = []
        for aster in asteroids:
            if aster < 0:
                if positive_stack:
                    not_break = True
                    while positive_stack:
                        if positive_stack[-1] < abs(aster):
                            positive_stack.pop()
                        elif positive_stack[-1] == abs(aster):
                            positive_stack.pop()
                            not_break = False
                            break
                        else:
                            not_break = False
                            break
                    
                    if not_break:
                        res.append(aster)
                else:
                    res.append(aster)
            else:
                positive_stack.append(aster)
                
        res.extend(positive_stack)
        
        return res