class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        heap = []
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        
        def getScore(words):
            score = 0
            
            for x in words.split(" "):
                if x in pos:
                    score += 3
                elif x in neg:
                    score -= 1
            
            return score
        
        for sid, words in zip(student_id, report):
            score = getScore(words)
            
            item = (score, -sid)
            
            if len(heap) == k:
                heappushpop(heap, item)
            else:
                heappush(heap, item)
        
        res = []
        
        while heap:
            score, sid = heappop(heap)
            sid = -sid
            res.append(sid)
        
        return res[::-1]