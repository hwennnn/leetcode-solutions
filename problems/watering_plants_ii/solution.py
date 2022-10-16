class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        res = 0
        deq = collections.deque(plants)
        alice, bob = capacityA, capacityB
        
        while deq:
            if len(deq) >= 2:
                left = deq.popleft()
                if alice < left:
                    res += 1
                    alice = capacityA
                
                alice -= left
                    
                
                right = deq.pop()
                if bob < right:
                    res += 1
                    bob = capacityB
                
                bob -= right
            else:
                last = deq.pop()
                
                m = max(alice, bob)
                
                if m < last:
                    res += 1
                    
        return res