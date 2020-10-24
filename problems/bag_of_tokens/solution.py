class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        deq = collections.deque(tokens)
        
        res = score = 0
        power = P
        
        while deq:
            if power >= deq[0]:
                power -= deq.popleft()
                score += 1
                res = max(res, score)
                continue
            
            if score >= 1:
                power += deq.pop()
                score -= 1
                continue
                
            break
                
        return res
                
            
            
            