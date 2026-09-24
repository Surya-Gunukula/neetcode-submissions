class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        currMinHeight = min(heights[i], heights[j])
        currMaxWater = (j - i) * currMinHeight 


        while(i < j):
            if(heights[j] > heights[i]):
                i += 1
                currMinHeight = min(heights[i], heights[j])
                currMaxWater = max(currMaxWater, (j-i) * currMinHeight)
            else:
                j -= 1
                currMinHeight = min(heights[i], heights[j])
                currMaxWater = max(currMaxWater, (j-i) * currMinHeight)
        
        return currMaxWater

        