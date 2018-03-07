#!/usr/bin/env python3

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows is 1:
            return s
        step = (numRows == 1) - 1  # 0 or -1  
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1: 
                step = -step  #change direction  
            idx += step
        return ''.join(rows)
        


if __name__ == "__main__":
    s = Solution()
    output = s.convert("PAYPALISHIRING", 3)
    print(output)
