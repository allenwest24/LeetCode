class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prev = -1
        ans = 0
        for ii in range(len(prices)):
            if prev > prices[ii]:
                prev = prices[ii]
            elif prev < prices[ii] and prev != -1:
                ans += prices[ii] - prev
                prev = prices[ii]
            prev = prices[ii]
                
        return ans
