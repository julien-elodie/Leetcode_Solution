"""Summary

TODO:
    Remain some problem
"""


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.traceback = {}
        self.solver = self.scanSolver()
        self.solve()

    def solve(self):
        if len(self.solver) == 0:
            return True
        pos = min(self.solver.keys(), key=lambda x: len(self.solver[x]))
        nums = self.solver[pos]
        for num in nums:
            self.traceback = {pos: self.solver[pos]}
            if self.fillCell(pos, num):
                if self.solve():
                    return True
            self.backTrack(pos)
        return False

    def scanSolver(self):
        fullfilled = list("123456789")
        helper, solver = {}, {}
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell != ".":
                    helper[("r", i)] = helper.get(("r", i), []) + [cell]
                    helper[("c", j)] = helper.get(("c", j), []) + [cell]
                    helper[(i // 3, j // 3)] = helper.get(
                        (i // 3, j // 3), []) + [cell]
                else:
                    solver[(i, j)] = []
        for (i, j) in solver.keys():
            filled = helper.get(("r", i), []) + helper.get(
                ("c", j), []) + helper.get((i // 3, j // 3), [])
            solver[(i, j)] = [num for num in fullfilled if num not in filled]
        return solver

    def fillCell(self, pos, val):
        self.board[pos[0]][pos[1]] = val
        del self.solver[pos]
        for (i, j) in self.solver.keys():
            if val in self.solver[(i, j)]:
                if i == pos[0] or j == pos[1] or (i / 3,
                                                  j / 3) == (pos[0] / 3,
                                                             pos[1] / 3):
                    self.traceback[(i, j)] = val
                    self.solver[(i, j)].remove(val)
                    if len(self.solver[(i, j)]) == 0:
                        return False
        return True

    def backTrack(self, pos):
        self.board[pos[0]][pos[1]] = "."
        for Pos in self.traceback:
            if Pos not in self.solver:
                self.solver[Pos] = self.traceback[Pos]
            else:
                self.solver[Pos].append(self.traceback[Pos])


if __name__ == "__main__":
    board = [[".", ".", "9", "7", "4", "8", ".", ".",
              "."], ["7", ".", ".", ".", ".", ".", ".", ".",
                     "."], [".", "2", ".", "1", ".", "9", ".", ".", "."],
             [".", ".", "7", ".", ".", ".", "2", "4",
              "."], [".", "6", "4", ".", "1", ".", "5", "9",
                     "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2",
              "."], [".", ".", ".", ".", ".", ".", ".", ".",
                     "6"], [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    output = s.solveSudoku(board)
    print(board)
