class Solution:
    def __init__(self):
        self.memo = {}
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (s1, s2, s3) in self.memo:
            return self.memo[(s1, s2, s3)]
        else:
            if s1 == '':
                self.memo[(s1, s2, s3)] = (s2 == s3)
                return self.memo[(s1, s2, s3)]
            elif s2 == '':
                self.memo[(s1, s2, s3)] = (s1 == s3)
                return self.memo[(s1, s2, s3)]
            else:
                if s1[0] == s3[0] and s2[0] == s3[0]:
                    self.memo[(s1, s2, s3)] = self.isInterleave(s1[1:], s2, s3[1:]) or\
                                                self.isInterleave(s1, s2[1:], s3[1:])
                    return self.memo[(s1, s2, s3)]
                elif s1[0] == s3[0]:
                    self.memo[(s1, s2, s3)] = self.isInterleave(s1[1:], s2, s3[1:])
                    return self.memo[(s1, s2, s3)]
                elif s2[0] == s3[0]:
                    self.memo[(s1, s2, s3)] = self.isInterleave(s1, s2[1:], s3[1:])
                    return self.memo[(s1, s2, s3)]
                else:
                    return False