class Solution:
    def countPaths(self, n, roads):
        G = defaultdict(list)
        
        for x, y, w in roads:
            G[x].append((y, w))
            G[y].append((x, w))

        dist = [float('inf')] * n
        dist[0] = 0
        cnt = [0]*n
        cnt[0] = 1
        heap = [(0, 0)]

        while heap:
            (min_dist, idx) = heappop(heap)
            if idx == n-1: return cnt[idx] % (10**9 + 7)
            for neib, weight in G[idx]:
                candidate = min_dist + weight
                if candidate == dist[neib]:
                    cnt[neib] += cnt[idx]

                elif candidate < dist[neib]:
                    dist[neib] = candidate
                    heappush(heap, (candidate, neib))
                    cnt[neib] = cnt[idx]