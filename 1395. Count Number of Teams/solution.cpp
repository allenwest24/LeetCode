class Solution {
public:
    int numTeams(vector<int>& rating) {
        int total = 0;
        int size = rating.size();
        for (int ii = 0; ii < size; ++ii) {
            for (int jj = ii + 1; jj < size; ++jj) {
                for (int kk = jj + 1; kk < size; ++kk) {
                    if ((rating[ii] < rating[jj] && rating[jj] < rating[kk]) || (rating[ii] > rating[jj] && rating[jj] > rating[kk])) {
                        ++total;
                    }
                }
            }
        }
        return total;
    }
};
