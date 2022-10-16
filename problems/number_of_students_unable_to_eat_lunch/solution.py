class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = collections.deque(students)
        
        for s in sandwiches:
            if s in queue:
                while queue[0] != s:
                    queue.append(queue.popleft())
                
                queue.popleft()
            
            else:
                return len(queue)
        
        return 0