class StockPrice:

    def __init__(self):
        self.records = collections.defaultdict(int)        
        self.t = -1
        self.maxHeap = []
        self.minHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price
        self.t = max(self.t, timestamp)
        heapq.heappush(self.maxHeap, (-price, timestamp))
        heapq.heappush(self.minHeap, (price, timestamp))

    def current(self) -> int:
        return self.records[self.t]

    def maximum(self) -> int:
        while self.maxHeap and self.records[self.maxHeap[0][1]] != -self.maxHeap[0][0]:
            heapq.heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.minHeap and self.records[self.minHeap[0][1]] != self.minHeap[0][0]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()