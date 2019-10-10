from functools import reduce

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        zigzag = [[None for _ in range(len(s) // 2 + len(s) % 2)] for _ in range(numRows)]

        tracked = 0
        i = 0
        j = 0
        while True:
            while i < numRows:
                if tracked == len(s):
                    break
                
                zigzag[i][j] = s[tracked]
                i += 1
                tracked += 1

            if tracked == len(s):
                break
            else:
                i -= 2
                j += 1

            while i >= 0:
                if tracked == len(s):
                    break
                
                zigzag[i][j] = s[tracked]
                i -= 1
                j += 1
                tracked += 1
            
            if tracked == len(s):
                break
            else:
                j -= 1
                i += 2

        
        res = []

        for row in zigzag:
            res.extend(filter(lambda x: x, row))

        return reduce(lambda x, y: x + y, res)
            