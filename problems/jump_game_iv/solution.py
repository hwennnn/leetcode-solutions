class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = collections.defaultdict(list)
        
        for i, x in enumerate(arr):
            graph[x].append(i)
        
        queue = collections.deque([(0, 0)])
        num_seen, pos_seen = set([0]), set()
        
        while queue:
            index, steps = queue.popleft()
            num = arr[index]
            
            if index == n - 1: 
                return steps
            
            for p in [index - 1, index + 1] + (graph[num] * (num not in num_seen)):
                if 0 <= p < n and p not in pos_seen:
                    queue.append((p, steps + 1))
                    pos_seen.add(p)
            
            num_seen.add(num)
        
        