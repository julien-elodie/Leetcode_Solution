class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums.count(target):
            return [-1, -1]
        sort = sorted(nums, reverse=True)
        return [nums.index(target), len(nums) - 1 - sort.index(target)]


if __name__ == "__main__":
    s = Solution()
    output = s.searchRange([5, 7, 7, 8, 8, 10], 8)
    print(output)