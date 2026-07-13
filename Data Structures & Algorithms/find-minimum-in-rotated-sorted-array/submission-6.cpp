class Solution {
public:
    int findMin(vector<int> &nums) {
        if(nums.size() == 1){
            return nums[0];
        }
        if(nums.size() == 2){
            if(nums[0] < nums[nums.size()-1]){
                return nums[0];
            }
            else{
                return nums[1];
            }
        }
        if(nums[0] < nums[nums.size()-1]){
            return nums[0];
        }

        int beg = 0;
        int end = nums.size();
        int mid = (beg+end)/2;
        while(mid < end && mid > beg){
            if(nums[mid+1] < nums[mid]){
                return nums[mid+1];
            }
            else if(nums[mid] < nums[mid-1]){
                return nums[mid]; 
            }
            else{
                if(nums[beg] < nums[mid]){
                    beg = mid;
                    mid = (beg+end)/2;
                }
                else{
                    end = mid; 
                    mid = (beg+end)/2;
                }
            }
        }
    }
};
