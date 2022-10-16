class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = collections.Counter(arr)
        
        for x, v in counter.items():
            if v == 1:
                k -= 1
                
                if k == 0: return x
        
        return ""