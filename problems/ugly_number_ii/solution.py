class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        if (n<=0): return 0
        if (n==1): return 1
        
        t2 =  t3 = t5 = 0 
        
        arr = [None] * n
        arr[0] = 1
        
        for i in range(1,n):
            
            arr[i] = min(arr[t2]*2, arr[t3]*3, arr[t5]*5)
            
            if arr[i] == arr[t2]*2: t2+=1
            if arr[i] == arr[t3]*3: t3+=1
            if arr[i] == arr[t5]*5: t5+=1
            
        return arr[-1]
        
            
                
            