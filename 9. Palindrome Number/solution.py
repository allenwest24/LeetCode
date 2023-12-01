class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for ii in range(len(s) // 2):
            if s[ii] != s[(-1 * (ii + 1))]:
                return False
        return True
