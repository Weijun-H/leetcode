# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode, ok=True) -> int:
        if not root: return 0
        l, r = self.maxPathSum(root.left, False), self.maxPathSum(root.right, False)
        self.max = max(getattr(self, 'max', float('-inf')), l + root.val + r)
        return self.max if ok else max(root.val + max(l, r), 0)

