class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        queue = deque(tokens)
        res = scores = 0
        
        while queue:
            if power >= queue[0]:
                power -= queue.popleft()
                scores += 1
                res = max(res, scores)
                continue
            
            if scores >= 1:
                power += queue.pop()
                scores -= 1
                continue
            
            break
        
        return res