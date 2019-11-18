class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = list(map(lambda ch: ch.lower(), filter(lambda ch: ch.isalpha() or ch.isnumeric(), list(s))))
        total_pos = 2 * len(alpha_num) - 1
        mid = total_pos // 2
        
        for offset in range(1, mid + 1):
            left = (mid - offset) / 2
            right = (mid + offset) / 2
            
            if (left % 1) == 0 and (right % 1) == 0:
                left = int(left)
                right = int(right)
                if alpha_num[left] != alpha_num[right]:
                    return False
                
        return True
        
        