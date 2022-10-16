class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = defaultdict(int)

        for a, b in roads:
            count[a] += 1
            count[b] += 1

        scores = defaultdict(int)
        
        v = sorted(count.items(), key = lambda x:-x[1])
        
        for k, cnt in v:
            scores[k] = n
            n -= 1
        
        res = 0
        
        for a, b in roads:
            res += scores[a] + scores[b]
        
        return res