class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        Digit_Map = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 1:
            return list(Digit_Map[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = Digit_Map[digits[-1]]
        return [s + c for s in prev for c in additional]


if __name__ == "__main__":
    s = Solution()
    output = s.letterCombinations("")
    print(output)
