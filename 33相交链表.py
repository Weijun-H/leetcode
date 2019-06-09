class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        p = []
        q = []
        while headA:
            p.append(headA)
            headA = headA.next
        while headB:
            q.append(headB)
            headB = headB.next
        count = -1
        target = None
        l1 = len(p)
        l2 = len(q)
        while -count<=l1 and -count<=l2:
            if q[count] == p[count]:
                target = p[count]
                count -= 1
            else:
                break
        return target
