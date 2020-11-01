class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n1 = len(arr)
        n2 = len(pieces)
        
        tmp = []
        for i in range(n1):
            tmp.append(arr[i])

            if tmp in pieces:
                tmp = []
        
        return len(tmp) == 0