class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        out.append(0)
        
        for ii in range(1, n + 1):
            out.append(out[ii & (ii - 1)] + 1)
        
        return out
