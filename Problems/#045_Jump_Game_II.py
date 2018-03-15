class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = lastIdx = nextIdx = 0
        while nextIdx < len(nums) - 1:
            ans += 1
            lastIdx, nextIdx = nextIdx, max(
                i + nums[i] for i in range(lastIdx, nextIdx + 1))
        return ans


if __name__ == "__main__":
    s = Solution()
    output = s.jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0])
    print(output)