class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False
        input_set = {nums[0]}

        for i in range(1, len(nums)):
            if(nums[i] in input_set):
                return True
            else:
                input_set.add(nums[i])
        return False
            
        