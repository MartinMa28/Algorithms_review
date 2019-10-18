class Solution:
    def maxArea(self, height: list) -> int:
        i = 0
        j = len(height) - 1
        vol = 0
        while i < j:
            if min((height[i], height[j])) * (j - i) > vol:
                vol = min((height[i], height[j])) * (j - i)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            
        
        return vol


if __name__ == "__main__":
    solu = Solution()
    print(solu.maxArea([2,3,4,5,18,17,6]))