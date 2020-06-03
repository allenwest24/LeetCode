class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int currMin = -1;
        int bestOutcome = 0;
        int size = prices.size();
        for (int ii = 0; ii < size; ++ii) {
            if (currMin == -1) {
                currMin = prices[ii];
            }
            else if (ii <= size - 1) {
                if (prices[ii] < currMin) {
                    currMin = prices[ii];
                }
                else if (prices[ii] - currMin > bestOutcome) {
                    bestOutcome = prices[ii] - currMin;
                }
            }
        }
        return bestOutcome;
    }
};
