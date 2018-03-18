class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [item for item in s.split(" ") if item]
        if s:
            return len(s[-1])
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    output = s.lengthOfLastWord("Hello World")
    print(output)