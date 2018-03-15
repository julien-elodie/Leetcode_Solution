class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        s_pointer, p_pointer = 0, 0
        match = 0
        star_index = -1
        while s_pointer < s_len:
            if p_pointer < p_len and (p[p_pointer] == "?"
                                      or s[s_pointer] == p[p_pointer]):
                s_pointer += 1
                p_pointer += 1
            elif p_pointer < p_len and p[p_pointer] == "*":
                star_index = p_pointer
                match = s_pointer
                p_pointer += 1
            elif star_index != -1:
                p_pointer = star_index + 1
                match += 1
                s_pointer = match
            else:
                return False
        while p_pointer < p_len and p[p_pointer] == "*":
            p_pointer += 1
        return p_pointer == p_len


if __name__ == "__main__":
    s = Solution()
    output = s.isMatch("aa", "a*a")
    print(output)