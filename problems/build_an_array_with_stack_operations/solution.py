class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = [i for i in range(1,n+1)]
        n = len(arr)
        res = []
        temp = []
        i = j = 0
        
        while temp != target:
            temp.append(arr[i])
            res.append("Push")
            if arr[i] != target[j]:
                temp.pop()
                res.append("Pop")
            else:
                j += 1
            i += 1
            
        return res
            
            
            
        