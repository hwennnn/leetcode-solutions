class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        res = [0] * n
        queue = deque([i for i in range(n)])
        
        deck.sort()
        
        for i in range(n):
            index = queue.popleft()
            res[index] = deck[i]
            if queue:
                queue.append(queue.popleft())
        
        return res
        