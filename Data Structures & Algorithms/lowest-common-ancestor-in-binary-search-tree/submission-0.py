# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(p.val == root.val or q.val == root.val):
            return root
        elif(p.val < root.val and q.val > root.val):
            return root
        elif(p.val < root.val and q.val < root.val):
            return self.dfs(root.left, p, q)
        else:
            return self.dfs(root.right, p, q)


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if(p.val < q.val):
            return self.dfs(root, p, q)
        else:
            return self.dfs(root, q, p)



        

        