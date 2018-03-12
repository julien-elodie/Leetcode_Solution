class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self.DFS(sorted(candidates), target, -1, [], ret)
        return ret

    def DFS(self, nums, target, index, path, ret):
        if target < 0:
            return
        if target == 0:
            if not ret.count(path):
                ret.append(path)
            return
        for index in range(index + 1, len(nums)):
            self.DFS(nums, target - nums[index], index, path + [nums[index]],
                     ret)


if __name__ == "__main__":
    s = Solution()
    output = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(output)