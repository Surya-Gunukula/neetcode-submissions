class Solution {
public:
    int rob(vector<int>& nums) {
        int N = nums.size(); 

        std::vector<int>dp(N);
        dp[0] = nums[0];
        dp[1] = std::max(nums[0], nums[1]);
        for(int i = 2; i < N; i++){
            dp[i] = std::max(nums[i] + dp[i-2], dp[i-1]);
        }

        return dp[N - 1];
    }
};
