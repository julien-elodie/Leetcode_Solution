#!/usr/bin/env python3


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        S = '#'.join("^{}$".format(s))
        l = len(S)
        P = [0] * l
        C = R = 0
        for i in range(1, l - 1):
            P[i] = min(R - i, P[2 * C - i]) if (R > i) else 0
            while S[i + 1 + P[i]] is S[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        maxLen, center = max(P), P.index(max(P))
        return s[(center - maxLen) // 2:(center + maxLen) // 2]


if __name__ == "__main__":
    s = Solution()
    output = s.longestPalindrome("babad")
    print(output)
