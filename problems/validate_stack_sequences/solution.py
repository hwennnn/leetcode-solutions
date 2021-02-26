class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]):
        n = len(pushed)
        deq = deque()
        right = j = 0
        
        for i,p in enumerate(pushed):
            if p == popped[j]: 
                right = i + 1
                j += 1
                break
            else:
                deq.append(p)

        while j < n:  
            if deq and deq[-1] == popped[j]:
                deq.pop()
                j += 1
            elif right < n:
                if pushed[right] == popped[j]:
                    right += 1
                    j += 1
                else:
                    deq.append(pushed[right])
                    right += 1
            else:
                return False
            
        return len(deq) == 0