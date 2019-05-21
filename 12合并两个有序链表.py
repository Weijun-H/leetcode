# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while l1 or l2:
            if l1 and l2:  # 两者非空
                tmp1 = l1.val
                tmp2 = l2.val
                if tmp1 < tmp2:
                    p.next = ListNode(tmp1)
                    l1 = l1.next
                else:
                    p.next = ListNode(tmp2)
                    l2 = l2.next
            elif l1:  # l2为空
                p.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:  # l1为空
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        return dummy.next
