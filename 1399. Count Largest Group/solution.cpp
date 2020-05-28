class Solution {
public:
    int countLargestGroup(int n) {
        unordered_map<int, int> map;
        int ms = 0, c = 0;
        for (int ii = 1; ii <= n; ii++) {
            int x = ii, sum = 0;
            while (x) {
                sum += x % 10;
                x = x / 10;
            }
            map[sum]++;
            if (ms < map[sum]) {
                ms = map[sum];
                c = 1;
            }
            else if(ms == map[sum])
                c++;
        }
        return c;
    }
};
