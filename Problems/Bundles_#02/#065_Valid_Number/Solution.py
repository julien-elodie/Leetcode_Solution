class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fsm = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
        fsm[0]['.'] = fsm[1]['.'] = fsm[2]['.'] = 4
        fsm[0]['+'] = fsm[0]['-'] = fsm[1]['+'] = fsm[1]['-'] = 2
        fsm[0][' '] = fsm[1][' '] = 1
        fsm[3]['.'] = fsm[6]['.'] = 7
        fsm[3]['e'] = fsm[3]['E'] = fsm[6]['e'] = fsm[6]['E'] = fsm[7][
            'e'] = fsm[7]['E'] = fsm[9]['e'] = fsm[9]['E'] = 8
        fsm[3][' '] = fsm[5][' '] = fsm[6][' '] = fsm[7][' '] = fsm[9][
            ' '] = fsm[11][' '] = 5
        fsm[8]['+'] = fsm[8]['-'] = 10
        for d in "0123456789":
            fsm[0][d] = fsm[1][d] = fsm[2][d] = 3
            fsm[3][d] = fsm[6][d] = 6
            fsm[4][d] = fsm[7][d] = fsm[9][d] = 9
            fsm[8][d] = fsm[10][d] = fsm[11][d] = 11
        state = 0
        for i in s:
            if not fsm[state].get(i):
                state = -1
                break
            state = fsm[state][i]
        return state == 3 or state == 5 or state == 6 or state == 7 or state == 9 or state == 11


if __name__ == "__main__":
    s = Solution()
    output = s.isNumber("0")
    print(output)
