class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution1
        nums = sorted(list(set([i for i in sorted(nums) if i > 0])))
        if not nums.count(1):
            return 1
        if max(nums) == len(nums):
            return max(nums) + 1
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if m + 1 == nums[m]:
                l = m
            else:
                r = m
        return nums[l] + 1
        # Solution2
        return min(set(range(1, len(nums) + 2)) - set([i for i in nums if i > 0]))


if __name__ == "__main__":
    s = Solution()
    output = s.firstMissingPositive([1, 2, 0])
    print(output)