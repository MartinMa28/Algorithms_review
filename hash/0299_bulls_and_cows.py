from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        secret_counter = defaultdict(int)
        guess_counter = defaultdict(int)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_counter[secret[i]] += 1
                guess_counter[guess[i]] += 1
                
        for key in secret_counter:
            if key in guess_counter:
                cows += min(secret_counter[key], guess_counter[key])
        
                
        return str(bulls) + 'A' + str(cows) + 'B'