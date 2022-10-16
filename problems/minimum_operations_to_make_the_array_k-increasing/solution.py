class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        A = collections.defaultdict(list)
        
        for i, x in enumerate(arr):
            A[i % k].append(x)
        
        res = 0
        for _, s in A.items():
            lis = []
            
            for x in s:
                index = bisect.bisect(lis, x)
                
                if index < len(lis):
                    lis[index] = x
                else:
                    lis.append(x)
            
            res += len(s) - len(lis)
        
        return res