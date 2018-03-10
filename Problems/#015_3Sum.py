class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
        res = list(res)
        res.sort()
        return res


if __name__ == "__main__":
    s = Solution()
    output = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(output)
