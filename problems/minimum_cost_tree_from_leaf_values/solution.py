class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        
        while len(arr) > 1:
            index = arr.index(min(arr))
            
            if 0 < index < len(arr) - 1:
                res += arr[index] * min(arr[index + 1], arr[index - 1])
            else:
                res += arr[index] * (arr[index + 1] if index == 0 else arr[index - 1])
            
            arr.pop(index)
        
        return res