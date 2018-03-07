import re


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return bool(re.findall(p, s).count(s))


if __name__ == "__main__":
    s = Solution()
    output = s.isMatch("aa", "a")
    print(output)
