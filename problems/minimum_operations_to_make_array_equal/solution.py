class Solution:
    def minOperations(self, s: int) -> int:
        
        arr = [(2*i) + 1 for i in range(s)]
        n = len(arr)

        if (n <= 1):
            return 0

        if (n == 2):
            return 1

        if n%2 == 1:
            ans = 1
            i = 0
            j = n-1
            ans = 0
            while (i != j):
                ans += (arr[j]-arr[i])//2
                i +=1
                j -=1
                
            return ans
        else:
            first_median = n//2
            second_median = first_median-1
            ans = 1
            i = 0
            j = n-1
            while (i != second_median or j != first_median):
                ans += (arr[j]-arr[i])//2
                i +=1
                j -=1
                
            return ans


        
        