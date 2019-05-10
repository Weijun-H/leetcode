# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cary = 0
        chain = ListNode(0)
        tail = chain
        while l1 != None or l2 != None:
            if l1 != None:
                x = l1.val
            else:
                x = 0
            if l2 != None:
                y = l2.val
            else:
                y = 0

            reminder = (x + y + cary) % 10
            cary = (x + y + cary) // 10
            temp = ListNode(reminder)
            chain.next = temp
            chain = temp
            if l1 != None:
                l1 = l1.next

            if l2 != None:
                l2 = l2.next
        if cary >= 1:
            chain.next = ListNode(1)
        return tail.next