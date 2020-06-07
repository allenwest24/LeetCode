// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        for (; n >= 0; --n) {
            n -= 9999;
            if (!isBadVersion(n) || n < 0) {
                int left = 10000;
                while (left) {
                    if (isBadVersion(n)) {
                        return n;
                    }
                    n += 1;
                    left -= 1;
                }
            }
        }
        return 0;
    }
};
