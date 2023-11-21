class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for x in s:
            if x.isalnum():
                new_s += x.lower()


        for ii in range(len(new_s) // 2):
            if new_s[ii] != new_s[-1 * (ii + 1)]:
                return False
        return True
        
