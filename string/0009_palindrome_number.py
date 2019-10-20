class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        
        for i in range(len(str_num) // 2):
            if str_num[i] != str_num[-i - 1]:
                return False
            
        return True