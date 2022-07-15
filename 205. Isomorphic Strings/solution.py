class Solution:
    def encode(slef, s: str) -> str:
        out = ""
        counter = 0
        for ii in range(len(s)):
            if ii == 0:
                out += str(counter)
                counter += 1
            elif s[ii] in s[:ii]:
                out += out[s.index(s[ii])]
            else:
                out += str(counter)
                counter += 1
        return out
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.encode(s) == self.encode(t)
