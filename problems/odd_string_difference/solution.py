class Solution:
    def oddString(self, words: List[str]) -> str:
        diff = defaultdict(list)
        
        for word in words:
            d = []
            
            for i in range(1, len(word)):
                d.append(ord(word[i]) - ord(word[i - 1]))
            
            diff[tuple(d)].append(word)
        
        for k, v in diff.items():
            if len(v) == 1:
                return v[0]