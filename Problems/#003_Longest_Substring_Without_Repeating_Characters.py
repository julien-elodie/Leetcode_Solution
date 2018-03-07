#!/usr/bin/env python3


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        maxLen = 0
        start = -1
        for i in range(len(s)):
            if dic.get(s[i]) is not None:
                start = max(start, dic[s[i]])
            dic[s[i]] = i
            maxLen = max(maxLen, i - start)
        return maxLen


if __name__ == "__main__":
    s = Solution()
    maxLen = s.lengthOfLongestSubstring("abcabcbb")
    print(maxLen)