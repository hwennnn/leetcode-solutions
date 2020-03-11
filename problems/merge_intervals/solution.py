class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2: return intervals
        
        intervals.sort(key = lambda x:(x[0],x[1]))
        
        output = []
        curr = intervals[0]
        output.append(curr)
        
        for interval in intervals[1:]:
            curr_start = curr[0]
            curr_end = curr[1]
            next_start = interval[0]
            next_end = interval[1]
            
            if curr_end >= next_start:
                curr[1] = max(curr_end,next_end)

            else:
                curr = interval
                output.append(curr)
            
        return output