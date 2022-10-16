from sortedcontainers import SortedList

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('inf')]
        res = 0
        
        sl = SortedList([(i, x) for i, x in enumerate(nums)])
        to_process = set()
        
        for index, (a, b) in enumerate(zip(nums, nums[1:])):
            if a > b:
                to_process.add((index + 1, b))
                
        while to_process:
            new_process = set()
            res += 1
            
            for j, b in to_process:
                index = sl.bisect_left((j, b))
                i, a = sl[index - 1]
                k, c = sl[index + 1]
                
                del sl[index]
                
                if a > c and (k, c) not in to_process:
                    new_process.add((k, c))
                
            
            to_process = new_process
        
        return res