class Solution:
    def canPlaceFlowers(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        
        for i in range(n):
            if arr[i] == 0:
                if i == 0 and i+1 < n and arr[i+1] == 0:
                    arr[i] += 1
                    k -= 1
                    continue

                if i == n-1 and arr[i-1] == 0:
                    arr[i] += 1
                    k -= 1
                    continue

                if 0 < i < n - 1 and arr[i] == arr[i-1] + arr[i+1]:
                    arr[i] += 1
                    k -= 1
        
        return k <= 0
                