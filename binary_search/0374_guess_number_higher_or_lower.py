class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1


if __name__ == "__main__":
    solu = Solution()
    solu.guessNumber(10)