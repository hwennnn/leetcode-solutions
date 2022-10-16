from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        M = 10 ** 9 + 7
        arr = SortedList()
        
        res = 0
        
        for num in instructions:
            l = arr.bisect_left(num)
            r = arr.bisect_right(num)
            
            res += min(l, len(arr) - r)
            res %= M
            arr.add(num)
        
        return res % M