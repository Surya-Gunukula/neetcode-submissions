class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index, height)

        for i, h in enumerate(heights):
            #print(maxArea)
            if(len(stack) == 0):
                stack.append((i, h))
                continue

            if(stack[-1][1] <= h):
                stack.append((i, h))
                continue

            while stack and stack[-1][1] > h: 
                leftI, leftH = stack.pop()
                area = leftH * (i - leftI)
                maxArea = max(area, maxArea)

                
            stack.append((leftI, h))

        for i, h in stack: 
            maxArea = max(maxArea, h * (len(heights) - i))
            

        return maxArea                
            


        

        