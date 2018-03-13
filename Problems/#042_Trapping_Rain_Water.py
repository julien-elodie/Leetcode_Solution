class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        ret = 0
        maxl, maxr = 0, 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= maxl:
                    maxl = height[l]
                else:
                    ret += maxl - height[l]
                l += 1
            else:
                if height[r] >= maxr:
                    maxr = height[r]
                else:
                    ret += maxr - height[r]
                r -= 1
        return ret


if __name__ == "__main__":
    s = Solution()
    output = s.trap([0,2,0])
    print(output)
