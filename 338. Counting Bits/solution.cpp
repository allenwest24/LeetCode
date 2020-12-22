class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> results;
        int power = 0;
        int starter = 1;
        int tmp = 0;
        int counter = 0;
        while (starter <= num) {
            starter *= 2;
            power++;
        }
        power--;
        for (int ii = 0; ii <= num; ii++) {
            counter = 0;
            tmp = ii;
            for (int jj = power; jj >= 0; jj--) {
                if (tmp >= pow(2, jj)) {
                    counter++;
                    tmp -= pow(2, jj);
                }
            }
            results.push_back(counter);
        }
        return results;
    }
};
