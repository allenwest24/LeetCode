class Solution:
    def makePrintableRange(self, a, b):
        if a == b:
            return str(b)
        return f"{a}->{b}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Initialize vars
        out = []
        curr_start = None
        prev = None

        # Go through and look at every number with context of previous and current start of range.
        for ii in range(len(nums)):
            curr = nums[ii]

            # If this is the very first run, we need to set the curr_start
            if curr_start is None:
                curr_start = curr
            # If this doesn't fit nicely in the current range, report the previous range, then start the new one.
            elif curr - 1 != prev:
                out.append(self.makePrintableRange(curr_start, prev))
                curr_start = curr

            # If this happens to be the last one, then just add what we have.
            if ii == len(nums) - 1:
                out.append(self.makePrintableRange(curr_start, curr))
                
            # No matter what, we want to update the curr
            prev = curr
        return out
