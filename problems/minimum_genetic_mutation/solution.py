class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = set([start])
        queue = deque([(start, 0)])
        bank = set(bank)
        
        while queue:
            word, count = queue.popleft()
            
            if word == end: return count
            
            for i in range(8):
                for char in "ACGT":
                    w = word[:i] + char + word[i + 1:]
                    if w not in visited and w in bank:
                        visited.add(w)
                        queue.append((w, count + 1))
        
        return -1