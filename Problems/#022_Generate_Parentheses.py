#!/usr/bin/env python3

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = set()
        if n == 0:
            return list(ret)
        elif n == 1:
            ret.add("()")
            return list(ret)
        else:
            for i in self.generateParenthesis(n - 1):
                    ret.add("(" + i + ")")
            for N in range(1, n):
                for i in self.generateParenthesis(n - N):
                    for j in self.generateParenthesis(N):
                        ret.add(i + j)
                        ret.add(j + i)
            l = list(ret)
            l.sort()
            return l 


if __name__ == "__main__":
    s = Solution()
    output = s.generateParenthesis(3)
    print(output)
