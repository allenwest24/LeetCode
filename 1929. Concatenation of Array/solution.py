class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for ii in range(len(nums) * 2):
            ans.append(nums[ii % len(nums)])
        return ans
