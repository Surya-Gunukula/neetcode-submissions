class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root

        for ch in word:
            if(ch not in currNode.children):
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]
        currNode.is_end = True
        
    def dfs(self, word: str, node: TrieNode) -> bool:
        for i in range(len(word)):
            if(word[i] == '.'):
                if(i == len(word) - 1):
                    for children in node.children.values():
                        if(children.is_end == True):
                            return True
                    return False
                for item in node.children:
                    currPath = self.dfs(word[i+1:], node.children[item])
                    if(currPath == True):
                        return True
                return False
            else:
                if(word[i] not in node.children):
                    return False
                else:
                    node = node.children[word[i]]
        return node.is_end

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)

        
