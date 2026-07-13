class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for(int num: nums){
            mp[num]++;
        }

        multimap<int, int, std::greater<int>> freq;
        for(auto& elem: mp){
            freq.insert({elem.second, elem.first});
        }

        vector<int> returnVec;
        auto it = freq.begin();
        for(int i = k; i>0; i--){
            returnVec.push_back(it->second);
            it++;
        }

        return returnVec;
    }
};
