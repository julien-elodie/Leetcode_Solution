#!/usr/bin/env python3


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        bracket = ""
        brackets = []
        for i in s:
            if i in "([{":
                bracket = bracket_map[i]
                brackets.append(i)
            elif i == bracket:
                brackets.pop()
                if brackets:
                    bracket = bracket_map[brackets[-1]]
            else:
                return False
        return not bool(brackets)


if __name__ == "__main__":
    s = Solution()
    # output = s.isValid("[")
    output = s.isValid("([])")
    print(output)
