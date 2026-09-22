# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        returnList = []

        if(root is None):
            return []
        queue.append(root)

        while(queue):
            returnList.append(queue[0].val)

            for i in range(len(queue)):
                currNode = queue.popleft()
                if(currNode.right is not None):
                    queue.append(currNode.right)
                if(currNode.left is not None):
                    queue.append(currNode.left)
        
        return returnList
            


            

        