class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def go(key):
            left = res = count = 0
            
            for right, x in enumerate(answerKey):
                if x == key:
                    count += 1
                
                while count > k:
                    if answerKey[left] == key:
                        count -= 1
                    left += 1
                
                res = max(res, right - left + 1)
            
            return res
        
        return max(go('T'), go('F'))