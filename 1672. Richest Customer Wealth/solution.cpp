class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int tmp, max;
        tmp = max = 0;
        for (int ii = 0; ii < accounts.size(); ii++) {
            for (int jj = 0; jj < accounts[ii].size(); jj++) {
                tmp += accounts[ii][jj];
            }
            if (tmp > max) {
                max = tmp;
            }
            tmp = 0;
        }
        return max;
    }
};
