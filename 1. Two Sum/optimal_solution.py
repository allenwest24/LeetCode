class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        # Stored as val:index.
        seen = {}
        for ii in range(len(nums)):
            if target - nums[ii] in seen:
                out.append(seen[target-nums[ii]])
                out.append(ii)
            else:
                seen[nums[ii]] = ii
        return out
