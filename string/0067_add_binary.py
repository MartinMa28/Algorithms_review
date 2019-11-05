class Solution:
    def _digit_add(self, a: str, b: str, carry: int):
        a = int(a)
        b = int(b)
        
        res = a + b + carry
        if res <= 1:
            return str(res), 0
        else:
            return str(res - 2), 1
    
    def addBinary(self, a: str, b: str) -> str:
        a = a.zfill(max((len(a), len(b))))
        b = b.zfill(max((len(a), len(b))))
        res = ''
        
        carry = 0
        for i in range(len(a)):
            digit, carry = self._digit_add(a[len(a) - i - 1], b[len(b) - i - 1], carry)
            res = digit + res
        
        if carry == 1:
            res = '1' + res
            
        return res
