class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        curr = 0
        for ii in nums:
            curr += ii
            out.append(curr)
        return out
