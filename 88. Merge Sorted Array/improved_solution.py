class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Instead of previous solution, we will replace in reverse, as this will reduce time complexity
        # of shifting elements and space complexity of storing certain segments of the merged list.

        # Main counter (reverse)
        ii = m + n -1
        # counter for m
        jj = m - 1
        # counter for n
        kk = n -1

        # Go until the last element, when it should be sorted. 
        # Update jj or kk when used, but always update ii
        while kk >= 0:
            # Pull from beginning half of nums1 if its the right choice.
            if jj >= 0 and nums1[jj] >= nums2[kk]:
                nums1[ii] = nums1[jj]
                jj -= 1
            # Otherwise pull from nums2
            else:
                nums1[ii] = nums2[kk]
                kk -= 1
            ii -= 1
