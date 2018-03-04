class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # get hash dict
        hash_dict = dict(zip(list(range(len(nums))), nums))
        for i, j in hash_dict.items():
            # drop duplicate
            if nums.count(target - j) and nums.index(target - j) != i:
                return [i, nums.index(target - j)] if i < nums.index(target - j) else [nums.index(target - j), i]
        # raise none
        return False

if __name__ == "__main__":
    s = Solution()
    output = s.twoSum([2,7,11,5],9)
    print(output)