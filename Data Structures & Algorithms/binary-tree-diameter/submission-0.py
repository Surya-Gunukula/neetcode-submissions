# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    global_max = -1

    def dfs(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        max_left_height = self.dfs(root.left)
        max_right_height = self.dfs(root.right)
        max_diameter = 1 + max_left_height + max_right_height

        if(max_diameter > self.global_max):
            self.global_max = max_diameter

        return 1 + max(max_left_height, max_right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        self.dfs(root)
        return self.global_max - 1
        
        