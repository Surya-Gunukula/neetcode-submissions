class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        std::map<std::string, bool> status_map;

        int n = s.size();

        for(int i = 0; i < wordDict.size(); i++){
            status_map[wordDict[i]] = true; 
        }

        vector<bool> dp(n+1, false);
        dp[0] = true;
        for(int i = 1; i <= n; i++){
            for(int j = 0; j < i; j++){
                if(dp[j]==true && status_map[s.substr(j, i-j)] == true) dp[i] = true;
            }
        }

        return dp[n] == true;
    }
};
