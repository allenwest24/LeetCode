class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for ii in range(len(nums)):
            curr = nums[ii]
            out.append(nums[curr])
        return out
