class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.DFS(sorted(candidates), target, 0, [], ret)
        return ret

    def DFS(self, nums, target, index, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for index in range(index, len(nums)):
            self.DFS(nums, target - nums[index], index, path + [nums[index]], ret)


if __name__ == "__main__":
    s = Solution()
    output = s.combinationSum([2, 3, 6, 7], 7)
    print(output)