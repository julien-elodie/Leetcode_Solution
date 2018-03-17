class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
        return max(nums)


if __name__ == "__main__":
    s = Solution()
    output = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(output)