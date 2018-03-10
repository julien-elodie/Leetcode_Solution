class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        remove = [i for i in nums if i != val]
        for i in range(len(remove)):
            nums[i] = remove[i]
        return len(remove)


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    s = Solution()
    output = s.removeElement(nums, 3)
    print(nums[:output])
