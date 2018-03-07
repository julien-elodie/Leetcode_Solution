#!/usr/bin/env python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeHelper:
    def __init__(self):
        pass

    def generate(self, list):
        """
        :type list: list
        :rtype: ListNode
        """
        N = node = ListNode(0)
        for i in list:
            node.next = ListNode(i)
            node = node.next
        return N.next

    def transform(self, node):
        """
        :type: ListNode
        :rtype list: list
        """
        ret = []
        while node:
            ret.append(node.val)
            node = node.next
        return ret

    def print(self, node):
        """
        :type node: ListNode
        """
        prt = []
        while node:
            prt.append(str(node.val))
            node = node.next
        print(" -> ".join(prt))


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        helper = ListNodeHelper()
        l1 = helper.transform(l1)
        l2 = helper.transform(l2)
        l = l1 + l2
        l.sort()
        return helper.generate(l)


if __name__ == "__main__":
    helper = ListNodeHelper()
    l1 = helper.generate([1, 2, 4])
    l2 = helper.generate([1, 3, 4])

    s = Solution()
    output = s.mergeTwoLists(l1, l2)
    helper.print(output)
