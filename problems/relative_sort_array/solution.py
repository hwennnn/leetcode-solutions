class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = collections.Counter(arr1) 
        s = set(arr2)
        res = []
        
        for num in arr2:
            res += [num] * mp[num]
        
        leftover = []
        for num in arr1:
            if num not in s:
                leftover.append(num)

        return res + sorted(leftover)