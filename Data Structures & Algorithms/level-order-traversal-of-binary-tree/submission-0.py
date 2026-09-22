# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        returnList = []

        if(root is None):
            return returnList
        
        queue.append(root)
        while(queue):
            levelList = []
            levelNumbers = []
            while(queue):
                tempNode = queue.popleft()
                levelList.append(tempNode)
                levelNumbers.append(tempNode.val)
            
            returnList.append(levelNumbers)
            for node in levelList:
                if(node.left is not None):
                    queue.append(node.left)
                if(node.right is not None):
                    queue.append(node.right)
        
        return returnList



        




        