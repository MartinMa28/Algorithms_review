from math import ceil

class Solution:
    
    @staticmethod
    def _count(A, B, idx) -> int:
        repeat = ceil((len(B) - len(A[idx:])) / len(A))
        A = A[idx:] + repeat * A
        
        for i in range(len(B)):
            if A[i] == B[i]:
                continue
            else:
                return -1
            
        return repeat + 1
    
    def repeatedStringMatch(self, A: str, B: str) -> int:
        '''
        abcd
        
        ab    cd abcd ab    cd
        
        cdabcdab
        find the starting point in A
        and check the rest of letters in B also exist at the next position in A
        '''
        if not B:
            return 0
        
        A_set = set(A)
        for ch in set(B):
            if ch not in A_set:
                return -1
        
        for idx, ch in enumerate(A):
            if ch == B[0]:
                res = self._count(A, B, idx)
                if res > 0:
                    return res
        
        return -1