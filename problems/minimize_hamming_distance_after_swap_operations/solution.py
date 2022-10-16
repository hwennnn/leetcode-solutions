class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        res = n = len(source)
        s = [set() for _ in range(n)]
        seen = [0] * n
        
        for a,b in allowedSwaps:
            s[a].add(b)
            s[b].add(a)
        
        def dfs(i):
            seen[i] = 1
            found.append(i)
            for j in s[i]:
                if not seen[j]:
                    dfs(j)
        
        for i in range(n):
            if seen[i]: continue
            
            found = []
            dfs(i)
            
            count1 = Counter(source[x] for x in found)
            count2 = Counter(target[x] for x in found)
            
            res -= sum((count1&count2).values())
            
        return res