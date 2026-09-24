class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        returnList = []
        while(i < n-1):
            target = -1 * nums[i]
            
            j, k = i+1, n-1
            while(j < k):
                if(nums[j] + nums[k] > target):
                    k -= 1
                elif(nums[j] + nums[k] < target):
                    j += 1
                else:
                    returnList.append([nums[i], nums[j], nums[k]])
                    while(j+1 < n and nums[j] == nums[j+1]):
                        j += 1
                    j += 1
            
            while(i+1 < n and nums[i] == nums[i+1]):
                i += 1
            i += 1
        

        return returnList

        