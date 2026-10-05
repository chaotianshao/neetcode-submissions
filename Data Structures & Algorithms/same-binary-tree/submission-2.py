# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode]
    ) -> bool:

        # Both are empty
        if p is None and q is None:
            return True

        # Only one is empty
        if p is None or q is None:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Compare left AND right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )
        