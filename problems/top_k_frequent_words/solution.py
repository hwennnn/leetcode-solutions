class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        A = list(counter.items())
        A.sort(key = lambda x: (-x[1], x[0]))
        
        return [x for x, _ in A[:k]]