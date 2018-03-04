class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not len(str):
            return 0
        ret = ""
        if str[0] in "+-":
            ret = ret + str[0]
        for i in range(len(ret), len(str)):
            if str[i].isdigit():
                ret += str[i]
            else:
                break
        try:
            int(ret)
        except ValueError:
            ret = 0
        else:
            ret = int(ret)
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if ret > MAX_INT:
            return MAX_INT
        if ret < MIN_INT:
            return MIN_INT
        else:
            return ret


if __name__ == "__main__":
    s = Solution()
    output = s.myAtoi("+1")
    print(output)
