class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        n = len(word)
        for i in range(n):
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()

            curr = curr.children[index]

        curr.end = True
        
    def search(self, word: str) -> bool:
        self.res = False
        
        self.dfs(self.root, word)
        
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.end: self.res = True
            
            return
        
        if self.isLastNode(node): return
        
        if word[0] == ".":
            for i in range(26):
                if node.children[i]:
                    self.dfs(node.children[i], word[1:])
            
        else:
            index = ord(word[0]) - ord('a')
            if node.children[index]:
                self.dfs(node.children[index], word[1:])

                    
    def isLastNode(self, node):
        for i in range(26):
            if node.children[i]: return False

        return True


        

    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)