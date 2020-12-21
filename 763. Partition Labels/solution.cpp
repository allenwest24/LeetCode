class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> partitions;
        char temp;
        int last = 0;
        for (int ii = 0; ii < S.length(); ii++) {
            temp = S[ii];
            for (int jj = ii + 1; jj < S.length(); jj++) {
                if (S[jj] == temp) {
                    last = jj;
                }
            }
            for (int kk = ii + 1; kk <= last; kk++) {
                for (int ll = last; ll < S.length(); ll++) {
                    if (S[kk] == S[ll]) {
                        last = ll;
                    }
                }
            }
            if (last > ii) {
                partitions.push_back(last - ii + 1);
                ii = last;
            }
            else {
               partitions.push_back(1);
            }
            last = 0;
        }
        return partitions;
    }
};
