class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Rules dictate there will be at least one item.
        minimum = nums[0]
        maximum = nums[0]
        best = nums[0]
        
        for ii in range(1, len(nums)):
            curr = [minimum * nums[ii], maximum * nums[ii], nums[ii]]
            minimum = min(curr)
            maximum = max(curr)
            if maximum > best:
                best = maximum
        
        return best
