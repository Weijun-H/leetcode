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
        num1 = 0
        num2 = 0
        i = 0
        while l1 != None:
            num1 += l1.val*pow(10,i)
            l1 = l1.next
            i += 1
        i = 0
        while l2 != None:
            num2 += l2.val*pow(10,i)
            l2 = l2.next
            i += 1
        num = num1 + num2
        nums = [int(x) for x in str(num)[::-1]]
        rtype = ListNode(nums[0])
        tail = rtype
        for i in nums[1:] :
            temp = ListNode(i)
            tail.next = temp
            tail= temp
        return rtype
