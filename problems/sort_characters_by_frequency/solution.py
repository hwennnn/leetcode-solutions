class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        buckets = [[] for _ in range(n + 1)]
        res = ''
        
        counter = collections.Counter(s)
        for k,v in counter.items():
            buckets[v].append(k)
        
        for i in range(n, -1, -1):
            for c in buckets[i]:
                res += c * i
        
        return res