from collections import Set


class Solution:
    def findAncestor(self, root: 'TreeNode', p: 'TreeNode', a):
        if not root: return
        a.insert(0, root)
        if root == p: return
        self.findAncestor(root.left, p, a) if p.val < root.val else self.findAncestor(root.right, p, a)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 把祖先存set.
        left = []
        self.findAncestor(root, p, left)
        right = []
        self.findAncestor(root, q, right)
        for i in left:
            if i in right:
                return i
        return None