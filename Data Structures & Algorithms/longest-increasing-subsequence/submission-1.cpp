class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int N = nums.size();
        vector<int>dp(N, 0);
        dp[0] = 1;
        for(int i = 1; i < N; i++){
            int temp_max = 0;
            for(int j = 0; j < i; j++){
                if(nums[i] > nums[j]) temp_max = std::max(temp_max, dp[j]);
            }
            dp[i] = temp_max + 1;
        }

        int final_max = 0;
        for(int i = 0; i < N; i++){
            if(dp[i] > final_max) final_max = dp[i];
        }

        return final_max;
    }
};
