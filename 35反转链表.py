# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        new_head = ListNode(0)
        if not head  :
            return head
        while head :
            nodes.append(head)
            head = head.next
        for i in nodes[::-1]:
            new_head.next = i
            new_head = i
        new_head.next = None
        return nodes[-1]