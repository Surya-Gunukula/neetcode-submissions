class Solution {
public:
    int solve(vector<int>& nums){
        int N = nums.size(); 

        std::vector<int>dp(N);
        dp[0] = nums[0];
        dp[1] = std::max(nums[0], nums[1]);
        for(int i = 2; i < N; i++){
            dp[i] = std::max(nums[i] + dp[i-2], dp[i-1]);
        }

        return dp[N - 1];
    }
    int rob(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        if(nums.size() == 1) return nums[0];

        std::vector<int> firsthouse(nums.begin(), nums.end() - 1);
        std::vector<int> lasthouse(nums.begin()+1, nums.end());

        return std::max(solve(firsthouse), solve(lasthouse));
    }
};
