class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        N = len(price)
        price.sort()
        
        def good(mid):
            pre = price[0]
            count = 1
            
            for i in range(1, N):
                if price[i] - pre >= mid:
                    count += 1
                    pre = price[i]
            
            return count >= k
        
        left, right = 0, 10 ** 9
        res = 0
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                res = mid
                left = mid + 1
            else:
                right = mid

        return res