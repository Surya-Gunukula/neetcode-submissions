class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        currNode = self.root

        for ch in word:
            if(ch not in currNode.children):
                currNode.children[ch] = TreeNode()
            currNode = currNode.children[ch]
        currNode.is_end = True
                
    def search(self, word: str) -> bool:
        currNode = self.root
        for ch in word:
            if(ch not in currNode.children):
                return False
            else:
                currNode = currNode.children[ch]
        
        if(currNode.is_end == True):
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for ch in prefix:
            if(ch not in currNode.children):
                return False
            else:
                currNode = currNode.children[ch]
        
        return True
        
        