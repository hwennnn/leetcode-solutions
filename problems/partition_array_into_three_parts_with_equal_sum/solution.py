class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)

        found = 0
        s = 0
        
        for x in arr:
            s += x
            if s == total // 3:
                s = 0
                found += 1
        
        return found >= 3