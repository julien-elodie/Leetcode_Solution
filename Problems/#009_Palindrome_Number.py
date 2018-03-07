#!/usr/bin/env python3


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    s = Solution()
    output = s.isPalindrome(0)
    print(output)