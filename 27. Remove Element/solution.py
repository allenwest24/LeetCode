class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ii = 0
        while ii < len(nums):
            if nums[ii] == val:
                del nums[ii]
                continue
            ii += 1
        return len(nums)
