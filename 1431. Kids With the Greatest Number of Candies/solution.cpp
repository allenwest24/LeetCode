class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int greatest = 0;
        vector<bool> returnVec;
        for (int ii = 0; ii < candies.size(); ++ii) {
            if (candies[ii] > greatest) {
                greatest = candies[ii];
            }
        }   
        for (int jj = 0; jj < candies.size(); ++jj) {
            returnVec.insert(returnVec.end(), candies[jj] + extraCandies >= greatest);
        }
        return returnVec;
    }
};
