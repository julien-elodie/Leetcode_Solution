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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        helper = ListNodeHelper()
        list = helper.transform(head)
        del list[-n]
        return helper.generate(list)


if __name__ == "__main__":
    # Helper
    helper = ListNodeHelper()
    head = helper.generate([1, 2, 3, 4, 5])

    s = Solution()
    output = s.removeNthFromEnd(head, 2)
    helper.print(output)
