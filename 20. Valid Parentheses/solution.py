class Solution:
    def isValid(self, s: str) -> bool:
        to_close = ""
        for ii in s:
            if ii == '(' or ii == '{' or ii == '[':
                to_close += ii
            else:
                if len(to_close) == 0:
                    return False
                elif (ii == ')' and to_close[-1] == '(') or (ii == '}' and to_close[-1] == '{') or (ii == ']' and to_close[-1] == '['):
                    to_close = to_close[:-1]
                else:
                    return False
        return True if len(to_close) == 0 else False
