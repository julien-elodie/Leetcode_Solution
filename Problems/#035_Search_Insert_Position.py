class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        return sorted(nums).index(target)


if __name__ == "__main__":
    s = Solution()
    output = s.searchInsert([1, 3, 5, 6], 2)
    print(output)