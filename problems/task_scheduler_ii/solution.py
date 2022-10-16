class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        n = len(tasks)
        last = defaultdict(lambda: -1)
        day = 1
        
        for task in tasks:
            if last[task] == -1 or day > last[task] + space + 1:
                last[task] = day
            else:
                day = last[task] + space + 1
                last[task] = day
                
            day += 1
            
        return day - 1