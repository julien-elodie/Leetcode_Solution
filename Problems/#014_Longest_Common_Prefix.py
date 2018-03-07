#!/usr/bin/env python3


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""
        l = [len(s) for s in strs]
        length = min(l)
        prefix = strs[l.index(length)]
        for s in strs:
            length = min(len(s), length)
            while prefix[:length] != s[:length]:
                length = length - 1
            prefix = prefix[:length]
        return prefix


if __name__ == "__main__":
    s = Solution()
    output = s.longestCommonPrefix(["a"])
    print(output)
