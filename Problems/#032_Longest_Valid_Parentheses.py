class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 1:
            return 0
        max_length = 0
        stack = [-1]
        for i in range(len(s)):
            top = stack[-1]
            if top != -1 and s[i] == ')' and s[top] == '(':
                stack.pop()
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)
        return max_length


if __name__ == "__main__":
    s = Solution()
    output = s.longestValidParentheses("()(()")
    print(output)