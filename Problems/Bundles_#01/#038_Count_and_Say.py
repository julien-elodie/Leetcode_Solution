class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "1"
        for i in range(n - 1):
            s = ""
            num = string[0]
            count = 1
            for j in range(len(string) - 1):
                if string[j + 1] == string[j]:
                    count += 1
                else:
                    s += str(count)
                    s += str(num)
                    num = string[j + 1]
                    count = 1
            s += str(count)
            s += str(num)
            string = s
        return string



if __name__ == "__main__":
    s = Solution()
    output = s.countAndSay(1)
    print(output)