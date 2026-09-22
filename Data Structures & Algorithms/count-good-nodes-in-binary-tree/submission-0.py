# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if(root is None):
            return 0

        numGoodNodes = 0
        queue = deque()
        queue.append((root, root.val))

        while(queue):
            for i in range(len(queue)):
                currNode, currMax = queue.popleft()
                if(currMax <= currNode.val):
                    numGoodNodes += 1
                    currMax = currNode.val
                if(currNode.left is not None):
                    queue.append((currNode.left, currMax))
                if(currNode.right is not None):
                    queue.append((currNode.right, currMax))
        
        return numGoodNodes
                


            
        