# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        # 链表个数
        num = 0
        p = head
        while p:
            num += 1
            p = p.next
        k = num - k % num
        p = head
        # 找前一段链表
        while k > 1:
            p = p.next
            k -= 1
        head1 = p.next
        if not head1: return head
        #前一段链表最后至空
        p.next = None
        p = head1
        # 后一段链表和前一段链表连接起来
        while p.next:
            p = p.next
        p.next = head
        return head1
if __name__ == '__main__':
    s = Solution()

