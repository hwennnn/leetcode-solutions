class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        n = len(arr)
        if n==2: return True
        
        def checkAcc(arr,n):
            diff = None
            arr.sort()
            for i in range(1, n):
                count = abs(arr[i]-arr[i-1])
                if i != 1 and diff != count:
                    return False
                diff = count

            return True
        
        def checkDesc(arr,n):
            diff = None
            arr.sort(reverse = True)
            for i in range(1, n):
                count = abs(arr[i]-arr[i-1])
                if i != 1 and diff != count:
                    return False
                diff = count

            return True
        
        return checkAcc(arr,n) or checkDesc(arr,n)
            
            
            