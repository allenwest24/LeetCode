class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_val = 0
        for ii in range(len(prices)):
            if ii == 0 or prices[ii] < buy_val:
                buy_val = prices[ii]
            if prices[ii] - buy_val > profit:
                profit = prices[ii] - buy_val
        # We are ok with making 0 trades if this would be the max profit possible.
        return profit
