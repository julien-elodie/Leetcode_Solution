#!/usr/bin/env python3


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    return sum
        return res


if __name__ == "__main__":
    s = Solution()
    output = s.threeSumClosest([0, 0, 0], 1)
    print(output)
