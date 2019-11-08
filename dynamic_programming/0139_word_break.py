class Solution:
    def __init__(self):
        self.memo = {}
    
    def wordBreak_top_down_memo(self, s: str, wordDict: list) -> bool:
        if s in self.memo:
            return self.memo.get(s)
        
        valid = False
        
        # iterate through all of position to split
        for i in range(0, len(s)):
            left_s = s[:i]
            right_s = s[i:]
            
            if left_s == '':
                if right_s in wordDict:
                    valid = True
                    break
            
            if left_s in wordDict and self.wordBreak_top_down_memo(right_s, wordDict):
                valid = True
                break
        
        self.memo[s] = valid
                
        return valid


    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for length in range(1, len(s) + 1):
            for i in range(0, length):
                if dp[i] and s[i: length] in wordDict:
                    dp[length] = True
                    break
        
        return dp[len(s)]