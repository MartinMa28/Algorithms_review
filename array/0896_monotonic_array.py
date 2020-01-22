class Solution:
    def isMonotonic(self, A: list) -> bool:
        prev = A[0]
        no_dup = [prev]

        for n in A[1:]:
            if n != prev:
                no_dup.append(n)
                prev = n

        A = no_dup
        
        if len(A) <= 1:
            return True
        
        increasing = (A[0] <= A[1])

        for i in range(1, len(A)):
            if increasing:
                if A[i - 1] > A[i]:
                    return False
            else:
                if A[i - 1] < A[i]:
                    return False

        return True