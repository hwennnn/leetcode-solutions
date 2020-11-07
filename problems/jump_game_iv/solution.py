class Solution:
    def minJumps(self, arr: List[int]) -> int:
        nei = collections.defaultdict(list)
        _ = [nei[v].append(i) for i,v in enumerate(arr)]
        
        pos_seen, num_seen = set(), set()
        deq = collections.deque([(0,0)])
        
        while deq:
            pos, step = deq.popleft()
            if pos == len(arr) - 1: return step
            num = arr[pos]
            pos_seen.add(pos)
            
            
            for p in [pos-1, pos+1] + nei[num] * (num not in num_seen):
                if not 0 <= p <= len(arr)-1 or p in pos_seen: continue
                deq.append((p, step+1))
            
            num_seen.add(num)
        