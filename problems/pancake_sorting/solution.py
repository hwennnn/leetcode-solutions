class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        largest = n
        res = []
        
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            
        
        for _ in range(n):
            index = arr.index(largest)
            reverse(0, index)
            reverse(0, largest - 1)
            res.append(index + 1)
            res.append(largest)
            largest -= 1
        
        return res