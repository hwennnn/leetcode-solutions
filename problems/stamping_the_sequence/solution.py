class Solution:
    def movesToStamp(self, stamp, target):
        m, n = len(stamp), len(target)
        masks = [(1<<m) - 1]*(n - m + 1)
        target_mask = (1<<n) - 1
        queue = deque()
        visited = set()
        for i in range(n - m + 1):
            for j in range(m):
                masks[i] ^= (1<<j)*(target[j+i] == stamp[j])
            if masks[i] == 0:
                visited.add(i)
                queue.append(i)
        
        ans = []
                
        while queue and target_mask != 0:
            cand = queue.popleft()
            ans.append(cand)
            to_update = [i for i in range(cand, min(n, cand + m)) if target_mask & (1<<i)]

            for i in to_update:
                for j in range(max(0, i - m + 1), min(i + 1, n - m + 1)):
                    masks[j] = masks[j] - (masks[j] & (1<<(i - j)))
                target_mask ^= (1<<i)

            for j in range(max(0, cand - m + 1), min(cand + m, n - m + 1)):
                if masks[j] == 0 and j not in visited:
                    visited.add(j)
                    queue.append(j)
        
        return ans[::-1] if target_mask == 0 else []