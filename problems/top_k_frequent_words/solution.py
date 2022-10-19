class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.word == other.word and self.freq == other.freq
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = []
        
        for word, freq in counter.items():
            heapq.heappush(heap, Word(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        
        return res[::-1]