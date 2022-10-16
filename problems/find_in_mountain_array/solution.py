# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length();
        peak = 0
        
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left
        
        left, right = 0, peak
        while left <= right:
            mid = (left + right) >> 1
            
            if mountain_arr.get(mid) > target:
                right = mid - 1
            elif mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                return mid
        
        left, right = peak, n - 1
        while left <= right:
            mid = (left + right) >> 1
            
            if mountain_arr.get(mid) < target:
                right = mid - 1
            elif mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                return mid
        
        return -1
        
        