class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        num = "%04d" % num
        return M[int(num[-4])] + C[int(num[-3])] + X[int(num[-2])] + I[int(
            num[-1])]


if __name__ == "__main__":
    s = Solution()
    output = s.intToRoman(1)
    print(output)
