class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int rtracker = 0;
        int ctracker = 0;
        vector<vector<int>> newnums;
        newnums.resize(r, vector<int>(c, 0));
        // If the resulting array is not possible, return the original nums.
        if (r * c != nums.size() * nums[0].size()) {
            return nums;
        }
        else {
            int curr = 0;
            for (int ii = 0; ii < nums.size(); ++ii) {
                for (int jj = 0; jj < nums[ii].size(); ++jj) {
                    curr = nums[ii][jj];
                    newnums[rtracker][ctracker] = curr;
                    if (ctracker < c - 1) {
                        ++ctracker;
                    }
                    else {
                        ctracker = 0;
                        ++rtracker;
                    }
                }
            }
            return newnums;
        }
        
    }
};
