class TrieNode:
    
    def __init__(self):
        self.hasWord = False
        self.children = collections.defaultdict(TrieNode)
    
    def hasEdge(self, char: str) -> bool:
        return char in self.children
    
    def get(self, char):
        return self.children[char]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for w in word:
            curr = curr.children[w]
        
        curr.hasWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        res = set()
        visited = set()
        
        for word in words:
            trie.insert(word)
        
        def go(x, y, curr, node):
            if node.hasWord:
                res.add(curr)
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited and node.hasEdge(board[dx][dy]):
                    visited.add((dx, dy))
                    go(dx, dy, curr + board[dx][dy], node.get(board[dx][dy]))
                    visited.remove((dx, dy))
            
        for x in range(rows):
            for y in range(cols):
                if trie.root.hasEdge(board[x][y]):
                    visited.add((x, y))
                    go(x, y, board[x][y], trie.root.get(board[x][y]))
                    visited.remove((x, y))
        
        return list(res)