#!/usr/bin/env python3

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        X = int(str(abs(x))[::-1])
        return ((x > 0) - (x < 0)) * X * (X < 2**31)


if __name__ == '__main__':
    s = Solution()
    output = s.reverse(123)
    print(output)
