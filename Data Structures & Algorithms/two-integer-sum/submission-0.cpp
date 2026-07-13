class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> returnVec;

        unordered_map<int, int> f_map;

        for(int i = 0; i < nums.size(); i++){
            if(f_map.find((target - nums[i])) != f_map.end()){
                int j = f_map[target - nums[i]];
                if(i < j){
                    returnVec.push_back(i);
                    returnVec.push_back(j);
                }
                else{
                    returnVec.push_back(j);
                    returnVec.push_back(i);
                }
                return returnVec;
            }
            else{
                f_map[nums[i]] = i;
            }
        }
    }
};
