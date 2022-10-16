class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i for i in range(1,m+1)]
        res = []
        for i,q in enumerate(queries):
            for j, num in enumerate(arr):
                if num == q:
                    res.append(j)
                    arr.pop(j)
                    arr.insert(0,num)
                    break
        
        return res