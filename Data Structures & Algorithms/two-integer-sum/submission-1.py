class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        input_map = {}
        for i in range(len(nums)):
            if(nums[i] in input_map):
                return [input_map[nums[i]], i]
            else:
                input_map[target - nums[i]] = i