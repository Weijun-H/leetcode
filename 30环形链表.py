# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        head_address = []
        temp = head
        while temp not in head_address:
            if temp is None:
                return False
            head_address.append(temp)
            temp = temp.next
        return True
