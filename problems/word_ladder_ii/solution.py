class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        s = set(wordList)
        mmin = float('inf')
        queue = collections.deque([[beginWord]])
        level = 1
        visited = set()

        while queue:
            ladder = queue.popleft()
            n = len(ladder)
            
            if n > level:
                for v in visited:
                    s.remove(v)
                visited.clear()
                
                if n <= mmin:
                    level = n
                else:
                    break
                    
            word = ladder[-1]
            for i in range(len(word)):
                for w in string.ascii_lowercase:
                    newWord = word[:i] + w + word[i + 1:]
                    if newWord in s:
                        visited.add(newWord)
                        if newWord == endWord:
                            minLevel = n + 1
                            res.append(ladder + [newWord])
                        else:
                            queue.append((ladder + [newWord]))
                
        return res