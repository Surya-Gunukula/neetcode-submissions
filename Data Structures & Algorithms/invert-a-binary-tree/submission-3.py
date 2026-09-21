# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root is None or (root.left is None and root.right is None)):
            return root
        elif(root.left is None):
            root.left = root.right 
            root.right = None
            self.invertTree(root.left)
        elif(root.right is None):
            root.right = root.left 
            root.left = None
            self.invertTree(root.right)
        else: 
            temp = root.right 
            root.right = root.left
            root.left = temp 
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root
        
        