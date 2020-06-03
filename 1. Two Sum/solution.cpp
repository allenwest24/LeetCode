class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> a{0, 0};
        int curr = 0;
        int size = nums.size();
        for (int ii = 0; ii < size; ++ii) {
            curr = nums[ii];
            for (int jj = ii + 1; jj < size; ++jj) {
                if (curr + nums[jj] == target) {
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
