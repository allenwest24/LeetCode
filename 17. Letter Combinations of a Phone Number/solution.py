class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        pad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        combinations = []
        for d in digits:
            curr_d = int(d)
            if len(combinations) == 0:
                for l in pad[curr_d]:
                    combinations += l
            else:
                temp_combo = []
                for ii in combinations:
                    for jj in pad[curr_d]:
                        to_add = ii
                        to_add += jj
                        temp_combo.append(to_add)
                combinations = temp_combo
        return combinations 
