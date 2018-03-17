class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setted = list(set(nums))
        setted.sort()
        for i in range(len(setted)):
            nums[i] = setted[i]
        return len(setted)


if __name__ == "__main__":
    nums = [1, 1, 2]
    s = Solution()
    output = s.removeDuplicates(nums)
    print(nums[:output])