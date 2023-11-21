class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ii = 0
        jj = 0
        for x in range(m+n):
            # If curr is best and nums1 isnt done yet.
            if jj >= n or (nums1[x] < nums2[jj] and ii < m):
                ii += 1
                continue
            else:
                temp = nums1[x:-1]
                nums1[x] = nums2[jj]
                nums1[x+1:] = temp
                jj += 1
