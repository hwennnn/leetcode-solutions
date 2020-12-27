class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = collections.defaultdict(list)
        _ = [graph[x].append(i) for i,x in enumerate(arr)]
        
        n = len(arr)
        deq = collections.deque([(0,0)])
        pos_seen, num_seen = {0}, set()
        
        while deq:
            pos, step = deq.popleft()
            
            if pos == n - 1: return step
            
            num = arr[pos]
            
            for p in [pos-1, pos+1] + graph[num] * (num not in num_seen):
                if not (0 <= p < n) or p in pos_seen: continue
                
                deq.append((p, step+1))
                pos_seen.add(p)
            
            num_seen.add(num)