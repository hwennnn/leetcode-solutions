class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        d = defaultdict(list)
        
        def go(x, y):
            if len(d[x]) == 3:
                heapq.heappushpop(d[x], (scores[y], y))
            else:
                heapq.heappush(d[x], (scores[y], y))
        
        for x, y in edges:
            go(x, y)
            go(y, x)
        
        res = float('-inf')
        
        for x, y in edges:
            for score1, node1 in d[x]:
                for score2, node2 in d[y]:
                    if node1 not in (x, y) and node2 not in (x, y) and node1 != node2:
                        res = max(res, scores[x] + scores[y] + score1 + score2)
        
        return -1 if res == float('-inf') else res