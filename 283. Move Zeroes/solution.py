class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = 0
        moved = 0
        while n + moved < len(nums):
            if nums[n] == 0:
                tmp = nums.pop(n)
                nums.append(tmp)
                moved += 1
            else:
                n += 1
