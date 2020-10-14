class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        phase2 = 0
        shift = -1
        for x in range(len(nums)):
            if nums[x] == target:
                phase2 = 1
                shift = 0
                if x > 0 and nums[x] < nums[x-1]:
                    return len(nums) - x + 1
            elif phase2 and nums[x] < target:
                shift += 1
        return shift
