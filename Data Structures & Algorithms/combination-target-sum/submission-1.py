class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(start):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            for i in range(start, len(nums)):
                if(nums[i] + sum(subset) > target):
                    break
                subset.append(nums[i])
                dfs(i)
                subset.pop()
        
        dfs(0)
        return res

        