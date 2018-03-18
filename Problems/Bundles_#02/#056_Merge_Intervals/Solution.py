# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class IntervalHelper:
    def generate(self, lists):
        """
        :type lists: List[List]
        :rtype: List[Interval]
        """
        ret = []
        for item in lists:
            interval = Interval(s=item[0], e=item[1])
            ret += [interval]
        return ret

    def transform(self, intervals):
        ret = []
        for interval in intervals:
            ret.append([interval.start, interval.end])
        return ret

    def printInretval(self, inretvals):
        """
        :type intervals: List[Interval]
        :rtype: None
        """
        ret = []
        for inretval in inretvals:
            ret += ["[" + str(inretval.start) + "," + str(inretval.end) + "]"]
        print(",".join(ret))


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        helper = IntervalHelper()
        intervals = sorted(helper.transform(intervals))
        for index in range(len(intervals) - 1):
            if intervals[index + 1][0] <= intervals[index][1]:
                merged = [
                    min(intervals[index][0], intervals[index + 1][0]),
                    max(intervals[index][1], intervals[index + 1][1])
                ]
                intervals[index] = None
                intervals[index + 1] = merged
        return helper.generate(
            [interval for interval in intervals if interval])


if __name__ == "__main__":
    helper = IntervalHelper()
    intervals = helper.generate([[1, 3], [2, 6], [8, 10], [15, 18]])

    s = Solution()
    output = s.merge(intervals)
    helper.printInretval(output)