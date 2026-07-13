class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False
        
        my_set = {nums[0]}
        
        for i in range(len(nums) - 1):
            if(nums[i+1] in my_set):
                return True
            else:
                my_set.add(nums[i+1])
        
        return False
        