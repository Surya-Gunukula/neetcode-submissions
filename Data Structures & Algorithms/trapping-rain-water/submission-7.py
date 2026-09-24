class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0
        wall, pending = 0, 0
        for j in range(1, n):
            if(height[j] >= height[wall]):
                wall = j
                total_water += pending
                pending = 0
            else:
                pending += height[wall] - height[j]
        
        right_wall, pending = 0, 0
        for i in range(n - 1, wall - 1, -1):
            if(height[i] >= right_wall):
                right_wall = height[i]
                total_water += pending
                pending = 0
            else:
                pending += right_wall - height[i]

        
        return total_water




        