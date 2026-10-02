class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        returnArr = [0] * n 

        for i, temp in enumerate(temperatures):
            if(len(stack) <= 0):
                stack.append((temp, i))
                continue
            while(len(stack) > 0 and stack[-1][0] < temp):
                pastTemp, pastI = stack.pop()
                returnArr[pastI] = i - pastI
            stack.append((temp, i))

        return returnArr
            


        