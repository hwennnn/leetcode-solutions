class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                if i == j: continue
                for k in range(n):
                    if i == k or j == k or digits[k] & 1: continue
                    res.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        
        return sorted(list(res))