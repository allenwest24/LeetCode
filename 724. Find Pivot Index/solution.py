class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totals = []
        curr = 0
        for ii in nums:
            curr += ii
            totals.append(curr)
        last = totals[-1]
        for jj in range(len(totals)):
            if totals[jj] - nums[jj] == (last - nums[jj]) / 2:
                return jj
        return -1
