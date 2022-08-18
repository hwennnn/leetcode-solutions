class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        A = sorted(counter.values())
        curr = n
        res = 0
        
        while A and curr > n // 2:
            curr -= A.pop() 
            res += 1
        
        return res