class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res


if __name__ == "__main__":
    s = Solution()
    output = s.maxArea([1, 1])
    print(output)
