# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pValue = []

        def dfs(root, sel):
            if root is None:
                if sel:
                    pValue.append(None)
                    return True
                else:
                    if not pValue:
                        return False
                    return pValue.pop(0) is None

            if sel:
                pValue.append(root.val)
            else:
                if not pValue:
                    return False

                value = pValue.pop(0)

                if value != root.val:
                    return False

            leftSide = dfs(root.left, sel)
            rightSide = dfs(root.right, sel)

            return leftSide and rightSide

        dfs(p, True)

        result = dfs(q, False)

        # q must consume everything stored from p
        return result and not pValue
            
