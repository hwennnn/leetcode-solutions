class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        temp = collections.Counter(arr)
        
        val = max(temp.values())
        
        for i in temp:
            if temp[i] == val:
        
                return i