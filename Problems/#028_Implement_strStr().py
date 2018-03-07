#!/usr/bin/env python3

import re


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        match = re.search(needle, haystack)
        if match:
            return match.span()[0]
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    output = s.strStr("hello", "ll")
    print(output)
