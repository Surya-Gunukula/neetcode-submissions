class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> outputString;

        unordered_map<string, vector<string>> f_map; 

        for (auto str : strs){
            vector<int> count(26, 0);
            for (char c: str){
                count[c - 'a']++;
            }

            string hashStr;
            for (int x: count){
                hashStr = hashStr + to_string(x) + "#"; 
            }

            f_map[hashStr].push_back(str);
        }

        for (auto pair : f_map){
            outputString.push_back(pair.second);
        }

        return outputString;
            
    }
};
