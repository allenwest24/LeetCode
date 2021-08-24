class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = ""
        curr = ""
        for c in range(len(s)):
            for c2 in range(c, len(s)):
                if s[c2] in curr:
                    if len(curr) > len(best):
                        best = curr
                    curr = ""
                    break
                else:
                    curr += s[c2]
            if len(curr) > len(best):
                best = curr
        print(best)
        return len(best)
