class SORTracker:

    def __init__(self):
        self.heap = []
        self.turns = 0

    def add(self, name: str, score: int) -> None:
        bisect.insort(self.heap, (-score, name))

    def get(self) -> str:
        _, name = self.heap[self.turns]
        self.turns += 1
        
        return name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()