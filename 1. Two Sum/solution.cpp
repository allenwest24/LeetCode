class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> a{0, 0};
        for (int ii = 0; ii < nums.size(); ++ii) {
            for (int jj = ii + 1; jj < nums.size(); ++jj) {
                if (nums[ii] + nums[jj] == target) {
                    a[0] = ii;
                    a[1] = jj;
                    return a;
                }
            }
        }
        // Should not get here
        return nums;
    }
};
