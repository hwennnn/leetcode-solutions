class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = collections.deque([(start, 0)])
        seen = set()
        
        while queue:
            x, steps = queue.popleft()
            
            for num in nums:
                operations = [x + num, x - num, x ^ num]
                for o in operations:
                    if o == goal: return steps + 1
                    if 0 <= o <= 1000 and o not in seen:
                        queue.append((o, steps + 1))
                        seen.add(o)
        
        return -1
            