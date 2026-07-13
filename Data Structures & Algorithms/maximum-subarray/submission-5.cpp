class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currTotal = nums[0];

        int bestScore = nums[0];

        if(nums.size() == 1) return bestScore;

        for(int i = 1; i < nums.size(); i++){
            if(nums[i] > currTotal && currTotal < 0){
                currTotal = nums[i];
            }
            else{
                currTotal += nums[i];
            }
            if(currTotal > bestScore){
                bestScore = currTotal;
            }
        }

        return bestScore;
    }
};
