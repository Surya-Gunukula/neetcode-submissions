# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isGlobalBalanced = True

    def dfs(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        maxLeftHeight = self.dfs(root.left)
        maxRightHeight = self.dfs(root.right)
        if(abs(maxLeftHeight - maxRightHeight) > 1):
            self.isGlobalBalanced = False
        return 1 + max(maxLeftHeight, maxRightHeight)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.isGlobalBalanced

        