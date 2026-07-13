class Solution {
public:
    string longestPalindrome(string s) {
        int N = s.size();
        vector<vector<int>>dp(N, std::vector<int>(N, false));

        int resLen = 0;
        int resInd = 0;

        for(int i = N-1; i >= 0; i--){
            for(int j = i; j < N; j++){
                if(s[i] == s[j] && (j - i <= 2 || dp[i+1][j-1] == true)){
                    dp[i][j] = true;
                    if(j - i + 1 > resLen){
                        resLen = j - i + 1;
                        resInd = i;
                    }
                } 
                
            }

        }

        return s.substr(resInd, resLen);

        

        

    }
};
