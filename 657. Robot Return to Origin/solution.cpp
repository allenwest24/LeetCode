class Solution {
public:
    bool judgeCircle(string moves) {
        int vert = 0;
        int horz = 0;
        for (char m:moves) {
            if (m == 'U') {
                vert++;
            }
            else if (m == 'D') {
                vert--;
            }
            else if (m == 'L') {
                horz--;
            }
            else if (m == 'R') {
                horz++;
            }
        }
        if (horz == 0 && vert == 0) {
            return true;
        }
        else {
            return false;
        }
    }
};
