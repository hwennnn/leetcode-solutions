class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        s = set(wordList)
        deq = collections.deque([(begin, 1)])
        visited = set()
        
        while deq:
            word, count = deq.popleft()
            if word == end: return count
            
            for i in range(len(word)):
                for x in string.ascii_lowercase:
                    w = word[:i] + x + word[i+1:] 

                    if w in s and w not in visited:
                        visited.add(w)
                        deq.append((w, count+1))
        
        return 0