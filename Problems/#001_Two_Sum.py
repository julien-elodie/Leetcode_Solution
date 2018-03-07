#!/usr/bin/env python3

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # get sorted dict
        sorted_dict = sorted(
            zip(list(range(len(nums))), nums), key=lambda item: item[1])
        l = 0
        r = len(nums) - 1
        while l < r:
            L = sorted_dict[l][1]
            R = sorted_dict[r][1]
            if L + R == target:
                return [sorted_dict[l][0], sorted_dict[r][0]]
            elif L + R < target:
                l = l + 1
            elif L + R > target:
                r = r - 1
        # raise none
        return False


if __name__ == "__main__":
    s = Solution()
    output = s.twoSum([2, 7, 11, 5], 9)
    print(output)
