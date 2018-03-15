class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for num in nums:
            ret = [
                item[:i] + [num] + item[i:] for item in ret
                for i in range((item + [num]).index(num) + 1)
            ]
        return ret


if __name__ == "__main__":
    s = Solution()
    output = s.permuteUnique([1, 1, 2])
    print(output)