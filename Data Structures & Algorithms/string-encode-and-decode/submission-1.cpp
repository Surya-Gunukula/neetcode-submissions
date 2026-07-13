class Solution {
public:

    string encode(vector<string>& strs) {
        string returnStr;

        for(auto str: strs){
            returnStr += (to_string(str.size()) + "#" + str);
        }

        std::cout << returnStr;
        return returnStr;
    }

    vector<string> decode(string s) {
        vector<string> returnVec;
        int i = 0; 
        int n = s.size();

        while(i < n){
            int j = i; 
            while(s[j] != '#' && j < n){
                j++;
            }

            int count = stoi(s.substr(i, j - i));

            string subs = s.substr(j+1, count);
            returnVec.push_back(subs);

            i = j + count + 1;
        }

        return returnVec;


    }
};
