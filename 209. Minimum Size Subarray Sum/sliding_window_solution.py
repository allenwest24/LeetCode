class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize a left index
        l = 0
        # Set the current total
        curr = 0
        # Create an infinite best so we can do easy compares
        best = float("inf")

        # Go through and sum until we get to the target
        for r in range(len(nums)):
            curr += nums[r]

            # When we hit the target, pull the l index with us until we are no longer at the target score
            # If our update of the left index is bad, we can continue with this new l value because if we 
            # Remained above the target value we wouldn't ever find a shorter subset.
            while curr >= target:
                # We can update the best if shorter because we are at target
                best = min(best, r-l+1)
                # Remove the leftmost value to see if we are still at target
                curr -= nums[l]
                # Update the left index
                l += 1
        
        # If we are still at infinity, return 0 as instructed, otherwise return the best we found.
        return 0 if best == float("inf") else best
