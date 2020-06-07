class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int size = nums.size();
        int oneFilled = 0;
        int twoFilled = 0;
        int threeFilled = 0;
        int one, two, three;
        int curr = 0;
        for (int ii = 0; ii < size; ++ii) {
            curr = nums[ii];
            cout << curr;
            if (curr > one || !oneFilled) {
                three = two;
                two = one;
                one = curr;
                if (twoFilled) {
                    threeFilled = 1;
                }
                else if (oneFilled) {
                    twoFilled = 1;
                }
                oneFilled = 1;
            }
            else if (curr > two && curr != one || (!twoFilled && curr != one)) {
                three = two;
                two = curr;
                if (twoFilled) {
                    threeFilled = 1;
                }
                twoFilled = 1;
            }
            else if (curr > three && curr != one && curr != two || (!threeFilled && curr != one && curr != two)) {
                three = curr;
                threeFilled = 1;
            }
        }
        if (!threeFilled) {
            return one;
        }
        else {
            return three; 
        }
    }
};
