class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        seen = set([start])
        bank = set(bank)
        dq = deque([start])
        count = 0

        while dq:
            N = len(dq)

            for _ in range(N):
                curr = dq.popleft()

                if curr == end: return count

                for i in range(8):
                    for char in "ACGT":
                        if char == curr[i]: continue
                        newWord = curr[:i] + char + curr[i + 1:]
                        if newWord in bank and newWord not in seen:
                            dq.append(newWord)
                            seen.add(newWord)
            
            count += 1
        
        return -1
