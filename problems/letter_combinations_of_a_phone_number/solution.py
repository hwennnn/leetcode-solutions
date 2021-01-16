class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        nums = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        deq = collections.deque([""])   
        
        for d in map(int, digits):
            tmp = []
            
            while deq:
                curr = deq.popleft()
                for digit in nums[d]:
                    tmp.append(curr+digit)
            
            for e in tmp:
                deq.append(e)

        
        return list(deq)