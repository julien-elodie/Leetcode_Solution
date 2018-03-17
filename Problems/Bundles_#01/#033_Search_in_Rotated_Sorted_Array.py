class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        sort = sorted(nums)
        shift = sort.index(nums[0])
        for i in range(len(sort)):
            if sort[i] == target:
                ret = i - shift
                return ret if ret >= 0 else len(nums) + ret
        return -1


if __name__ == "__main__":
    s = Solution()
    # output = s.search([], 5)
    output = s.search([3, 1], 1)
    print(output)
