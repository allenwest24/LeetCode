class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int sum = 0;
        int gs = grid.size();
        for (int ii = 0; ii  < gs; ++ii) {
            for (int jj = 0; jj < gs; ++jj) {
                if (grid[ii][jj] < 0) {
                    sum += (gs - jj);
                    break;
                }
            }
        }
        return sum;
    }
};
