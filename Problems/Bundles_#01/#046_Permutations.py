class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            ret = []
            for item in nums:
                copy = nums[:]
                copy.remove(item)
                ret += [i + [item] for i in self.permute(copy)]
            return sorted(ret)
        

if __name__ == "__main__":
    s = Solution()
    output = s.permute([1, 2, 3])
    print(output)