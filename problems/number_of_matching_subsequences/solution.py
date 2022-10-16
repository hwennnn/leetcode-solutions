class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mp = collections.defaultdict(collections.deque)
        
        for w in words:
            mp[w[0]].append(w)
        
        res = 0
        
        for c in s:
            n = len(mp[c])
            
            for _ in range(n):
                word = mp[c].popleft()
                if len(word) == 1:
                    res += 1
                else:
                    mp[word[1]].append(word[1:])
        
        return res