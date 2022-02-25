class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        A = map(int, version1.split('.'))
        B = map(int, version2.split('.'))
        
        for v1, v2 in zip_longest(A, B, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
                
            
        return 0
            