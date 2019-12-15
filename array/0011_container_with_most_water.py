class Solution:
    def maxArea(self, height: list) -> int:
        # greedy solution
        left = 0
        right = len(height) - 1
        most = 0
        
        while left < right:
            most = max((most, min((height[left], height[right])) * (right - left)))
            
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
                
        return most


if __name__ == "__main__":
    solu = Solution()
    print(solu.maxArea([2,3,4,5,18,17,6]))