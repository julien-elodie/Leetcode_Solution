class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.matrix = matrix
        self.ret = []
        self.sprial()
        return self.ret

    def sprial(self):
        if not self.matrix:
            return []
        self.rows, self.cols = len(self.matrix), len(self.matrix[0])
        m = min(self.rows, self.cols)
        if m == 0:
            return
        elif self.rows == 1:
            self.ret += self.matrix[0]
            return
        elif self.cols == 1:
            self.ret += [i[0] for i in self.matrix]
            return
        else:
            self.ret += self.matrix[0]
            for i in range(1, self.rows - 1):
                self.ret.append(self.matrix[i][self.cols - 1])
            self.ret += self.matrix[self.rows - 1][::-1]
            for i in range(self.rows - 2, 0, -1):
                self.ret.append(self.matrix[i][0])
            self.matrix = [
                matrix[1:self.cols - 1]
                for matrix in self.matrix[1:self.rows - 1]
            ]
        self.sprial()


if __name__ == "__main__":
    s = Solution()
    output = s.spiralOrder([[1, 11]])
    print(output)