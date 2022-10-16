class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], extra: int) -> int:
        res = 0
        A = []
        
        for cap, rock in zip(capacity, rocks):
            if cap == rock:
                res += 1
                continue
            
            A.append(cap - rock)
        A.sort()
        
        for x in A:
            if extra >= x:
                res += 1
                extra -= x
            else:
                break
        
        return res