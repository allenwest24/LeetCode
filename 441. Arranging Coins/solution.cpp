class Solution {
public:
    int arrangeCoins(int n) {
        int nextHeight = 0;
        while (n > nextHeight) {
            ++nextHeight;
            n -= nextHeight;
        }
        return nextHeight;
    }
};
