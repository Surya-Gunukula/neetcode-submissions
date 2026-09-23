class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list, suffix_list = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_list[i] = prefix_list[i-1] * nums[i-1]
            suffix_list[len(nums) - i - 1] = suffix_list[len(nums) - i] * nums[len(nums) - i]

        return [x * y for x, y in zip(prefix_list, suffix_list)]

        