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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        helper = ListNodeHelper()
        head = helper.transform(head)
        for i in range(len(head) // k + 1):
            head[k * (i - 1):k * i] = head[k * (i - 1):k * i][::-1]
        return helper.generate(head)


if __name__ == "__main__":
    helper = ListNodeHelper()
    head = helper.generate([1, 2, 3, 4, 5], 2)
    s = Solution()
    output = s.swapPairs(head)
    helper.print(output)
