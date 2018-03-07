#!/usr/bin/env python3


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    s = Solution()
    output = s.removeDuplicates(nums)
    print(nums[:output])