class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        pre = [0] * n
        paths = [n + 1] * (1 << n)
        target = (1 << n) - 1
        
        for x, y in relations:
            x -= 1
            y -= 1
            pre[y] |= (1 << x)
        
        queue = deque([(0, 0)])
        
        while queue:
            state, steps = queue.popleft()
            new_courses = []
            
            for i in range(n):
                if (state & pre[i]) != pre[i]: continue
                
                if state & (1 << i) > 0: continue
                
                new_courses.append(i)
            
            if len(new_courses) <= k:
                for course in new_courses:
                    state |= (1 << course)
                
                if state == target: return 1 + steps
                
                if steps + 1 < paths[state]:
                    queue.append((state, steps + 1))
                    paths[state] = steps + 1
            else:
                for comb in combinations(new_courses, k):
                    new_state = state
                    
                    for course in list(comb):
                        new_state |= (1 << course)
                    
                    if steps + 1 < paths[new_state]:
                        queue.append((new_state, steps + 1))
                        paths[new_state] = steps + 1