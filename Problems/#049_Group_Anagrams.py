class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for string in strs:
            key = ''.join(sorted(string))
            if ret.get(key):
                ret[key] += [string]
            else:
                ret[key] = [string]
        return [sorted(ret[key]) for key in ret.keys()]


if __name__ == "__main__":
    s = Solution()
    output = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(output)