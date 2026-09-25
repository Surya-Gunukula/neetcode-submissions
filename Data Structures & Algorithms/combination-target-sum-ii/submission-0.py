class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        
        def dfs(start):
            if(sum(subset) == target):
                res.append(subset.copy())
                return
            for i in range(start, len(candidates)):
                if(sum(subset) + candidates[i] > target):
                    break
                if(i > start and candidates[i] == candidates[i - 1]):
                    continue          
                subset.append(candidates[i])
                dfs(i + 1)
                subset.pop()
                            
        dfs(0)
        return res
        