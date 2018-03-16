class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n


if __name__ == "__main__":
    s = Solution()
    output = s.myPow(2.00000, 10)
    print(output)