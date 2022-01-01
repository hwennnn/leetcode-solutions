class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        
        def distance(s1, s2):
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i + 1
            
            return 1
        
        n = len(words)
        weights = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                weights[i][j] = distance(words[i], words[j])
                weights[j][i] = distance(words[j], words[i])
        
        dp = [[0] * n for _ in range(1 << n)]
        
        queue = collections.deque([(i, 1 << i, 0, [i]) for i in range(n)])
        completedMask = (1 << n) - 1
        max_overlap, max_path = -1, []
        
        while queue:
            node, mask, overlap, path = queue.popleft()
            
            if dp[mask][node] > overlap: continue
            
            if mask == completedMask and overlap > max_overlap:
                max_overlap, max_path = overlap, path
                continue
            
            for nei in range(n):
                if mask & (1 << nei): continue
                    
                next_mask = mask | (1 << nei)
                old = dp[next_mask][nei]
                new = dp[mask][node] + weights[node][nei]

                if new > old:
                    dp[next_mask][nei] = new
                    queue.append((nei, next_mask, new, path + [nei]))
                        
        res = words[max_path[0]]
        
        for i in range(1, n):
            prev, curr = max_path[i - 1], max_path[i]
            overlap = weights[prev][curr] - 1
            res += words[curr][overlap:]
        
        return res
            