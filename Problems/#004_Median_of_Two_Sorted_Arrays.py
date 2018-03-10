class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        half = len(nums) // 2
        return (nums[half] + nums[~half]) / 2


if __name__ == "__main__":
    s = Solution()
    median = s.findMedianSortedArrays([1, 3], [2])
    print(median)