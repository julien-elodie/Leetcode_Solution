#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = l = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            carry = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, mod = divmod(carry, 10)
            cur.next = ListNode(mod)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return l.next


if __name__ == "__main__":
    """
    l1 : 2 -> 4 -> 3
    l2 : 5 -> 6 -> 4
    """
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # solution
    s = Solution()
    l = s.addTwoNumbers(l1, l2)
    print(str(l.val) + " -> " + str(l.next.val) + " -> " + str(l.next.next.val))
