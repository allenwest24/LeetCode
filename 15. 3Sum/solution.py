class Solution:
    def twoSum(self, ii, nums, out):
        left = ii + 1
        right = len(nums) - 1
        
        while not left == right:
            curr = nums[ii] + nums[left] + nums[right]
            if curr == 0:
                if not [nums[ii], nums[left], nums[right]] in out:
                    out.append([nums[ii], nums[left], nums[right]])
                left += 1
            elif curr > 0:
                right -= 1
            elif curr < 0:
                left += 1
 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        
        ii = 0
        while ii < len(nums) - 1 and nums[ii] <= 0:
            if ii == 0 or not nums[ii] == nums[ii - 1]:
                self.twoSum(ii, nums, out)
            ii += 1
        return out
