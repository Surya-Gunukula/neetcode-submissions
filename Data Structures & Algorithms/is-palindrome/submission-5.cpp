class Solution {
public:
    bool isPalindrome(string s) {
        string s_fixed;
        for(int i = 0; i < s.size(); i++){
            if(isalnum(s[i])){
                s_fixed += tolower(s[i]);
            }
        }
        std::cout << s_fixed;
        for(int i = 0; i < (s_fixed.size()/2); i++){
            if(s_fixed[i] != s_fixed[s_fixed.size() - 1 - i]){
                return false;
            }
        }

        return true;
    }
};
