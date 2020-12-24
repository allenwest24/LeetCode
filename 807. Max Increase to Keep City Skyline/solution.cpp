// This solution is not the fastest, but uses less memory than if you were to save
// the top down view in an array in order to avoid traversing arrays so much. 
// Either solution feels grimey to me.
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int xMax, yMax, curr, total;
        xMax = yMax = total = 0;
        for (int ii = 0; ii < grid.size(); ii++) {
            for (int jj = 0; jj < grid[ii].size(); jj++) {
                xMax = yMax = 0;
                curr = grid[ii][jj];
                for (int kk = 0; kk < grid[ii].size(); kk++) {
                    if (xMax < grid[ii][kk]) {
                        xMax = grid[ii][kk];
                    }
                }
                for (int ll = 0; ll < grid.size(); ll++) {
                    if (yMax < grid[ll][jj]) {
                        yMax = grid[ll][jj];
                    }
                }
                
                // Set the current spot to the lesser of the two maxes.
                yMax > xMax ? grid[ii][jj] = xMax : grid[ii][jj] = yMax;
                total += grid[ii][jj] - curr;
            }
        }
        return total;
    }
};
