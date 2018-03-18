class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastIdx = nextIdx = 0
        while nextIdx < len(nums) - 1:
            lastIdx, nextIdx = nextIdx, max(
                i + nums[i] for i in range(lastIdx, nextIdx + 1))
            if lastIdx == nextIdx:
                break
        return nextIdx >= len(nums) - 1


if __name__ == "__main__":
    s = Solution()
    output = s.canJump([3, 2, 1, 1, 4])
    print(output)