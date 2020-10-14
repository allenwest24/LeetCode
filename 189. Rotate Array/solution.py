class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = 0
        for ii in range(k):
            temp = nums[len(nums)-1]
            nums.insert(0, temp)
            nums.pop()
        return nums
