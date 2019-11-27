class Solution:
    def trap(self, height: list) -> int:
        left_to_right = [0 for _ in range(len(height))]
        right_to_left = [0 for _ in range(len(height))]
        
        max_value = 0
        for i in range(len(height)):
            max_value = max((max_value, height[i]))
            left_to_right[i] = max_value
            
        max_value = 0
        for i in range(len(height) - 1, -1, -1):
            max_value = max((max_value, height[i]))
            right_to_left[i] = max_value
            
        water = 0
        
        for i in range(len(height)):
            water += (min((left_to_right[i], right_to_left[i])) - height[i])
            
        return water