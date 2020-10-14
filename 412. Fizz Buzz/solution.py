class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        save = []
        for ii in range(1, n+1):
            tmp = ""
            if ii % 3 == 0:
                tmp += "Fizz"
            if ii % 5 == 0:
                tmp += "Buzz"
            if len(tmp) == 0:
                tmp += str(ii)
            save.append(tmp)
        return save
