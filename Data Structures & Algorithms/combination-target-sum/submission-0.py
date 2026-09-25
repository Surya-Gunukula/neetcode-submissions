class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(start, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break
                subset.append(nums[i])
                dfs(i, remaining - nums[i])
                subset.pop()
        
        dfs(0, target)
        return res

        