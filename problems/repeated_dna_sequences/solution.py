class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = collections.defaultdict(int)
        n = len(s)
        if n < 10: return []
        word = s[:10]
        mp[word] += 1
        word = deque(word)
        
        for i in range(10, n):
            word.popleft()
            word += s[i]
            
            mp["".join(word)] += 1
        
        res = []
        for word, count in mp.items():
            if count > 1:
                res.append(word)
        
        return res